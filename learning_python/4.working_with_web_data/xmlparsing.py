# 
# Example file for parsing and processing XML
#

import xml.dom.minidom as xml

def main():
    # Use the parse() function to load and parse an XML file
    doc = xml.parse("samplexml.xml")
    
    # Print out the document node and the name of the first child tags
    print(doc.nodeName)
    print(doc.firstChild.tagName)
    
    # Get a list of XML tags from the document and print each one
    skills = doc.getElementsByTagName("skill")
    print("Skills: {0}".format(skills.length))
    for s in skills:
        print("\t {0}".format(s.getAttribute("name")))
    
    # Create a new XML tag and add it into the document
    newSkill = doc.createElement("skill")
    newSkill.setAttribute("name", "jQuery")
    doc.firstChild.appendChild(newSkill)

    skills = doc.getElementsByTagName("skill")
    print("Skills: {0}".format(skills.length))
    for s in skills:
        print("\t {0}".format(s.getAttribute("name")))

if __name__ == "__main__":
    main()
