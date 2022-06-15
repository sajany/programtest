import os

# Environment variables
BUCKET_NAME = os.getenv('BUCKET_NAME')
BUCKET_REGION = os.getenv('BUCKET_REGION')
NODE_V2_URL = os.getenv('NODE_V2_URL')
AUTH_HEADER = os.getenv('AUTH_HEADER')

# Supportive constants
S3_HOME = f'https://{BUCKET_NAME}.s3.amazonaws.com/'

# Node APIs
GET_INVOICE_LABELS_URL = f'{NODE_V2_URL}/attachment/getInvoiceLabels?invoiceId='
SAVE_INVOICE_LABEL_URL = f'{NODE_V2_URL}/attachment/saveInvoiceLabels'
UPDATE_INVOICE_LABEL_URL = f'{NODE_V2_URL}/attachment/updateInvoiceLabels'

# Node API Header
API_V2_HEADER = {
    'authorization': AUTH_HEADER,
    'Content-Type': 'application/json'
}