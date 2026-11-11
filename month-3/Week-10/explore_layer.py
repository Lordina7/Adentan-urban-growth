import geopandas as gpd

wards = gpd.read_file("Data/processed/wards.gpkg", layer="wards")

print(wards.head())
print("rows and columns:", wards.shape)
print(wards.geom_type.value_counts())
print("CRS:", wards.crs)
print("Bounds:" , wards.total_bounds)