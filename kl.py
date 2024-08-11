from lxml import etree

# Load XML
xml_file = 'products.xml'
xsl_file = 'transform.xsl'
xsd_file = 'products.xsd'

# Parse the XML
xml_doc = etree.parse(xml_file)

# Transform with XSL
xsl_doc = etree.parse(xsl_file)
transform = etree.XSLT(xsl_doc)
html_doc = transform(xml_doc)

# Save the HTML
with open('output.html', 'w') as f:
    f.write(str(html_doc))

# Validate with XSD
xsd_doc = etree.parse(xsd_file)
xmlschema = etree.XMLSchema(xsd_doc)

try:
    xmlschema.assertValid(xml_doc)
    print("XML is valid according to the XSD schema.")
except etree.DocumentInvalid as e:
    print(f"XML is invalid: {e}")
