These files were generated using ArcMap
For the ditance rasters the Euclidain Distance tool was used
For the density rasters the Kernel Density tool was used
The output rasters were set to the same spacial resolution and extent

We chose to proccess the apartments using this raster method to simplify the computations.
This way we do most of the calculations on the server side and the client side only has to 
do some basic math to encourperate the users preferences and generate the score.

Also this method allows us to aviod using a ton of ESRI online credits. 
We have hundereds of apartments and hundereds of features to measusre the distance to
Instead of doing all these calculations we save distance and density rasters beforehand 
and use them to generate the criteria for the apartments afterwards.