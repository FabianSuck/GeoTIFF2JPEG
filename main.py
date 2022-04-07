from osgeo import gdal

gdal.UseExceptions()

parent = iface.mainWindow()

inp,inpOk=QFileDialog.getOpenFileNames(parent,"Dateien auswaehlen", QgsProject.instance().homePath(),"GeoTIFF(*.Tif)")

driver = gdal.GetDriverByName("COG")
# COG= Cloud Optimized GeoTIFF generator
driver.Register()
translate_options = gdal.TranslateOptions(gdal.ParseCommandLine("-of COG -co COMPRESS=JPEG"))

for in_path in inp:
      src_ds = gdal.Open((in_path))
      out_path=in_path+"._COG.tif"
      gdal.Translate(out_path,src_ds,options=translate_options)
      print("Erfolgreich konvertiert {}...".format(in_path))

QMessageBox.information(parent, "Erfolgreich", "Erfolgreich konvertiert {}...".format(inp))
print("Hat funktioniert!")
