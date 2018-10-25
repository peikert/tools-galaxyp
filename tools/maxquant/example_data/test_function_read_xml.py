# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 16:28:36 2018

@author: cpeikert
"""

from string import Template

s = Template('$who likes $what')
s.substitute(who='Tim', what='proteomics')

#%% Cell
Test

##
#%% mqPar Parser
import xml.etree.ElementTree as ET
tree = ET.parse('D:\git\MQuant_Console\mqpar.xml')


for elem in tree.getiterator():
    print(elem.tag, elem.attrib)
    break
    
root = tree.getroot()

root.tag
root.attrib
root.keys
#
#

#root.findall('owl:Class', namespaces)
#.attrib['key']
#for name in root.attrib:
#    print('{0}="{1}"'.format(name, root.attrib[name]))
#root.tag
#
#for child in root:
#    print(child.tag, child.attrib)
#    if(child.tag == 'filePaths'):
#        rs = get_all_childen_as_list(child)

#        break
    
def get_all_childen_as_list(node):
    temp_dict = []
    if(len(node.getchildren())):
        for child in node:
            print(child.tag, child.attrib, child.text)  
            temp_dict.append({'id':child.tag, 'value': get_all_childen_as_list(child)})
 #           temp_dict.append({id:child.tag, 'value': child})
    else:
        temp_dict.append({'id':node.tag, 'value': node.text})
    return(temp_dict)



mqpar_list = [{'id': root.tag, 'value':get_all_childen_as_list(root)}]










type(mqpar_list[0]['value'])
type(mqpar_list[0]['value'][0])
mqpar_list[0]['value'][0]['value'][0]['value'] is None


output_file = open('test.xml','w')
nested_list = mqpar_list[0]
def nested_list_to_text(nested_list, depth):
#        print(depth)
#        if(nested_list['id']=='variationParseRule /'):
#            print('!!!!!!!!!!!!!!!')
        if(type(nested_list['value'])!=list):
#            print('$$$')
#            print(nested_list['id'])
#            print(nested_list['value'])
#            1+1
          return(str(nested_list['value'])+'\n')
#          return(''.join(['  '*depth,'<',nested_list['id'],'>',str(nested_list['value']),'</',nested_list['id'],'>\n']))
#          output_file.flush()
#            if(nested_list['value'] is None):
#                print('!!!!!!!!')
##                print('<',nested_list['id'],' />\n')
#            else:
#                ''.join(['<',nested_list['id'],'>',str(nested_list['value']),'</',nested_list['id'],'>\n'])
        else:
            if(nested_list['value'][0]['value'] is None):
                output_string = '   '*(depth-2)
            else:
                output_string = '   '*depth
                if(len(nested_list['value'])==1):
                    output_string += '<'+nested_list['id']+'>'
                else:
                    output_string += '<'+nested_list['id']+'>\n'
            for nl in nested_list['value']:
#                print(nested_list['id'])
#                if(nested_list['id']=='variationParseRule'):
#                    print('!!!')
#                    break
                if(nested_list['value'][0]['value'] is None):
#                    ''.join(['<',nested_list['id'],' />\n'])
                    output_string += ''.join(['   '*depth,'<',nested_list['id'],' />\n'])
#                    output_file.flush()
                else:
#                    ''.join(['<',nested_list['id'],'>',str(nested_list_to_text(nl)),'</',nested_list['id'],'>\n'])
#                    print(''.join(['<',nested_list['id'],'>',str(nested_list_to_text(nl)),'</',nested_list['id'],'>\n']), end='')
                    output_string += nested_list_to_text(nl,(depth+1))
            
            if(not nested_list['value'][0]['value'] is None):
                if(len(nested_list['value'])==1):
                    output_string = output_string.strip('\n')
                    output_string += '</'+nested_list['id']+'>\n'
                else:
                    output_string += '   '*depth+'</'+nested_list['id']+'>\n'
                 
            return(output_string)                   
        
#print(nested_list_to_text(mqpar_list[0],0))


output_string = '<?xml version="1.0" encoding="utf-8"?>\n'
output_string += nested_list_to_text(mqpar_list[0],0)
output_file.write(output_string)
output_file.close()   


     