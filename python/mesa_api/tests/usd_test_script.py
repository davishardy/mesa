from pxr import Usd, UsdGeom, Gf, Sdf

# Create a new stage (USD file)
stage = Usd.Stage.CreateNew('simple_scene.usda')

# Define a root Xform (transform node) at the stage
xform = UsdGeom.Xform.Define(stage, '/root')

# Create a cube under the Xform
cube = UsdGeom.Cube.Define(stage, '/root/cube')

# Set cube attributes (size and transform)
cube.GetSizeAttr().Set(2.0)  # Cube size of 2 units
xform.AddTranslateOp().Set(Gf.Vec3f(0, 0, 0))  # Set translation to (0, 0, 0)

# Save the stage
stage.GetRootLayer().Save()

print("USD file saved: simple_scene.usda")

