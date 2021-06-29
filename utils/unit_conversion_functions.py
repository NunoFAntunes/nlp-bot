from quantulum3 import parser

async def check_for_units(message):
    text = message.content
    parser.parse(text)