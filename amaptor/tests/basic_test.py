"""
	Just runs some of the code while initial api is being developed - real tests to follow
"""

import amaptor

ARCGIS_PRO_DOCUMENT = r"C:\Users\dsx.AD3\Documents\ArcGIS\Projects\MyProject2\MyProject2.aprx"
ARCGIS_PRO_LAYER = "GenerateWQLayer3"
ARCGIS_PRO_NEAR = "GenerateMonth10"

ARCMAP_DOCUMENT = r"C:\Users\dsx.AD3\Projects\flood\valmeyer_digitizing_working.mxd"
ARCMAP_LAYER = "merged_nfhl_no500_nominimal"
ARCMAP_NEAR = "merged_nfhl_no500_nominimal selection"

def BasicTest(path=ARCGIS_PRO_DOCUMENT, find_layer=ARCGIS_PRO_LAYER, near_layer=ARCGIS_PRO_NEAR):
	# in the long run, it won't matter which starting document we use because we'll convert Pro projects to MXDs and vice versa
	project = amaptor.Project(path)
	l_map = project.maps[0]
	l_map.find_layer(name=find_layer)
	layer = l_map.find_layer(name=find_layer)
	l_map.insert_layer_by_name_or_path(layer, near_name=near_layer)
	project.save()

def ArcMapTest():
	BasicTest(ARCMAP_DOCUMENT, ARCMAP_LAYER, ARCMAP_NEAR)

if __name__ == "__main__":
	BasicTest()