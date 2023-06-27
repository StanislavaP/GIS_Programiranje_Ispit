import geopandas as gpd
import matplotlib.pyplot as plt

CLC = gpd.read_file(r'C:\Users\perko\OneDrive\Desktop\Programiranje-Ispit\CLC18 SRB UTM.shp')
Srb = gpd.read_file(r'C:\Users\perko\OneDrive\Desktop\Programiranje-Ispit\OpstineSrb-UTM.shp')
print("Current Projection:", Srb.crs)
print("Current Projection:", CLC.crs)
cicevac_opstina = Srb[Srb['Opstina'] == 'Cicevac']

intersection = gpd.overlay(CLC, cicevac_opstina, how='intersection')
dissolved1 = intersection.dissolve(by='code_18').reset_index()

code_18_values = ['112', '131', '211', '321', '231', '242', '243', '311', '321','324','411', '511']
color_palette = ['#ff0000', '#a600cc','#ffffa8','#e68000','#e6e64d','#ffe64d','#e6cc4d',"#80ff00",'#ccf24d','#a6f200','#a6a6ff','#00ccf2']

value_color_map = {value: color_palette[i] for i, value in enumerate(code_18_values)}

dissolved1['color'] = dissolved1['code_18'].map(value_color_map).fillna('gray')
dissolved1.plot(color=dissolved1['color'])
plt.show()

output_path = r'C:\Users\perko\OneDrive\Desktop\Programiranje-Ispit\dissolved1.shp'
dissolved1.to_file(output_path)