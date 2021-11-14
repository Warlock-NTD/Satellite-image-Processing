# from pathlib import Path
from osgeo import ogr, gdal, osr




#relative = Path("mydir/Exercise 1-20211023T165507Z-001/Exercise 1/vnm_pd_2020_1km_UNadj.tif")
#absolute = relative.absolute()  # absolute is a Path object
dataset = gdal.Open('MCD12Q1_LC_Type1.tif', gdal.GA_ReadOnly)

def printGeo(dataset):
    print("Driver: {}/{}".format(dataset.GetDriver().ShortName, dataset.GetDriver().LongName))
    print("Size is {} x {} x {}".format(dataset.RasterXSize, dataset.RasterYSize, dataset.RasterCount))
    print("Projection is {}".format(dataset.GetProjection()))
    geotransform = dataset.GetGeoTransform()
    if geotransform:
        print("Origin = ({}, {})".format(geotransform[0], geotransform[3]))
        print("Pixel Size = ({}, {})".format(geotransform[1], geotransform[5]))

# print(dataset.GetGeoTransform())
# printGeo(dataset)
print(dataset.GetProjection())
"""
# band1 = dataset.GetRasterBand(1).ReadAsArray()
# print(band1)
# print(dataset.GetGeoTransform())
# print(dataset.GetProjection())
# Gdal.GetDriverByName(str).Create(name, size_x, size_y, band_number, data_type)
# Dataset.SetGeoTransform(geotransform)
# dataset.SetProjection(projection)
# Dataset.GetRasterBand(n).WriteArray(data)
# Dataset.FlushCache()
"""
"""
VectorDriver = ogr.GetDriverByName('ESRI Shapefile')
VectorDataset = VectorDriver.Open('Hanoi.shp', 0) # 0=Read-only, 1=Read-Write
layer = VectorDataset.GetLayer()
FeatureCount = layer.GetFeatureCount()
Count = 0
for feature in layer:
    Count += 1
    geom = feature.GetGeometryRef()
    minX, maxX, minY, maxY = geom.GetEnvelope()
    print(minX, maxX, minY, maxY)
    OutTileName = str(Count) + '.SomeTileName.tif'
    OutTile = gdal.Warp(OutTileName, dataset, format='GTiff', outputBounds=[minX, minY, maxX, maxY], xRes=0.5, yRes=0.5,
                        dstSRS=dataset.GetProjectionRef(),
                        resampleAlg=gdal.GRA_NearestNeighbour, options=['COMPRESS=DEFLATE'])

# ds = gdal.Translate('new.tif', dataset, projWin = [105.199, 106.423, 105.356, 106.267])
"""
"""
OutTile = gdal.Warp('new.tif', dataset, format='GTiff', outputBounds=[105.199, 106.423, 105.356, 106.267],
                        dstSRS=dataset.GetProjectionRef(), xRes=0.0083333333, yRes=0.0083333333,
                        resampleAlg=gdal.GRA_NearestNeighbour, options=['COMPRESS=DEFLATE'])
"""
"""
o_srs = osr.SpatialReference()
o_srs.ImportFromEPSG(32648)
# print(o_srs)
# o_srs.SetLinearUnits(o_srs, 'Meter', 1.0)

minX, minY, maxX, maxY = 513880.656, 2265149.043, 657152.818, 2381433.65
g_options = gdal.WarpOptions(xRes=30, yRes=-30, resampleAlg=gdal.GRA_NearestNeighbour,
                             outputBounds=[minX, minY, maxX, maxY])
gdal.Warp('new.tif', dataset, dstSRS=o_srs, options=g_options)
"""


# dataset : 1781 x 879

