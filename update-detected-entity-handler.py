import json
import boto3
import utils
import requests

import get_invoice_label_handler
import create_invoice_label_handler
import update_invoice_label_handler

def handle(event, context):
    print(event)

    request_method = event.get('requestContext', {}).get('http', {}).get('method')
    if request_method == 'OPTIONS':
        return
    
    request_event = json.loads(event.get('body'))
    invoice_id = request_event.get('invoiceId')
    updated_entities = request_event.get('entityDatasetDetails')
    create_update_invoice_labels(invoice_id, updated_entities)
    
    return {
        'body': json.dumps({
            'success': True
        }),
        'statusCode': 200
    }

def create_update_invoice_labels(invoice_id, updated_entities):
    invoice_labels = get_invoice_label_handler.handle(invoice_id)

    save_labels = []
    update_labels = []
    for entity in updated_entities:
        field_name = entity.get('fieldName')
        target_variable = entity.get('targetVariable')
        invoice_label = invoice_labels.get(target_variable)
        
        if invoice_label is None:
            save_labels.append({
                'labelType': target_variable,
                'label': field_name,
                'detectedLabel': 'N/A'
            })
        else:
            update_labels.append({
                'labelType': target_variable,
                'label': field_name,
                'detectedLabel': invoice_label.get('detectedLabel')
            })

    print(f'New labels chosen by user {save_labels}')
    print(f'Existing labels modified by user {update_labels}')
    
    if len(save_labels) > 0:
        create_invoice_label_handler.handle({
            'invoiceId': invoice_id,
            'invoiceLabels': save_labels
        })
    if len(update_labels) > 0:
        update_invoice_label_handler.handle({
            'invoiceId': invoice_id,
            'invoiceLabels': update_labels
        })

    return None
