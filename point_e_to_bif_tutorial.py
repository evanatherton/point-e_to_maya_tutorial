import replicate
import os

import maya.cmds as cmds


API_KEY = ''  # Make a Replicate account and get an API key https://replicate.com/account and paste it here
os.environ['REPLICATE_API_TOKEN'] = API_KEY


def replicate_point_e(prompt, output_format='json_file'):
    model = replicate.models.get("cjwbw/point-e")
    version = model.versions.get("1a4da7adf0bc84cd786c1df41c02db3097d899f5c159f5fd5814a11117bdf02b")

    inputs = {'prompt': prompt, 'output_format': output_format}

    output = version.predict(**inputs)
    
    return output['json_file']
    

def point_e():    
    data = None
    
    result = cmds.promptDialog(
		title='Point-e',
		message='Enter Prompt:',
		button=['Cancel', 'OK'],
		text='a vase of purple flowers',
		defaultButton='OK',
		cancelButton='Cancel',
		dismissString='Cancel')

    if result == 'OK':
	    text = cmds.promptDialog(query=True, text=True)
	    data = replicate_point_e(text)
	    	    
	    
    return data
    

def point_e_to_bif(point_e_data):
    bif_graph = cmds.ls(type='bifrostGraphShape')[0]
    
    
    color_data = point_e_data['colors']
    point_positions = point_e_data['coords']
    
    color_data_str = ','.join([str(item) for point in color_data for item in point])
    point_positions_str = ','.join([str(item) for point in point_positions for item in point])
    
    cmds.vnnNode(bif_graph, "/{}".format('point_e_color_data'), setPortDefaultValues=('value', '{{{}}}'.format(color_data_str)))
    cmds.vnnNode(bif_graph, "/{}".format('point_e_point_positions'), setPortDefaultValues=('value', '{{{}}}'.format(point_positions_str)))
    
    

data = point_e()

if data:
    point_e_to_bif(data)

