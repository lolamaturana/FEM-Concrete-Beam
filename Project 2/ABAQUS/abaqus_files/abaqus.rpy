# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2025 replay file
# Internal Version: 2024_09_20-06.00.46 RELr427 198590
# Run by mbd2171 on Wed Dec 17 08:09:33 2025
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=345.333312988281, 
    height=241.380004882812)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.ModelFromInputFile(name='NACA4424_Airfoil2', 
    inputFileName='C:/Users/mbd2171/Downloads/NACA4424_Airfoil2.inp')
#: The model "NACA4424_Airfoil2" has been created.
#: The part "MATLAB_MESH" has been imported from the input file.
#: The model "NACA4424_Airfoil2" has been imported from an input file. 
#: Please scroll up to check for error and warning messages.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['NACA4424_Airfoil2'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
p1 = mdb.models['NACA4424_Airfoil2'].parts['MATLAB_MESH']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.95136, 
    farPlane=2.16367, width=1.35689, height=0.752369, viewOffsetX=0.151509, 
    viewOffsetY=0.00522874)
s = mdb.models['NACA4424_Airfoil2'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=175.899, 
    farPlane=201.225, width=173.427, height=96.1623, cameraPosition=(12.1852, 
    2.71758, 188.562), cameraTarget=(12.1852, 2.71758, 0))
s.unsetPrimaryObject()
del mdb.models['NACA4424_Airfoil2'].sketches['__profile__']
p1 = mdb.models['NACA4424_Airfoil2'].parts['MATLAB_MESH']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.95136, 
    farPlane=2.16367, width=1.35689, height=0.752369, viewOffsetX=0.110171, 
    viewOffsetY=0.0125266)
p = mdb.models['NACA4424_Airfoil2'].parts['MATLAB_MESH']
p.DatumPointByCoordinate(coords=(0.0, 0.0, 0.0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.91484, 
    farPlane=2.20019, width=1.82168, height=1.01009, viewOffsetX=0.287496, 
    viewOffsetY=0.0221063)
p = mdb.models['NACA4424_Airfoil2'].parts['MATLAB_MESH']
p.DatumPointByCoordinate(coords=(0.0, 0.0, 0.0))
p1 = mdb.models['NACA4424_Airfoil2'].parts['MATLAB_MESH']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
mdb.models['NACA4424_Airfoil2'].parts['MATLAB_MESH'].setValues(
    space=TWO_D_PLANAR, type=DEFORMABLE_BODY)
s1 = mdb.models['NACA4424_Airfoil2'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.rectangle(point1=(-0.5, -0.5), point2=(1.5, 0.5))
p = mdb.models['NACA4424_Airfoil2'].Part(name='plate', 
    dimensionality=TWO_D_PLANAR, type=DEFORMABLE_BODY)
p = mdb.models['NACA4424_Airfoil2'].parts['plate']
p.BaseShell(sketch=s1)
s1.unsetPrimaryObject()
p = mdb.models['NACA4424_Airfoil2'].parts['plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['NACA4424_Airfoil2'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.29038, 
    farPlane=4.65389, width=2.28005, height=1.26425, viewOffsetX=0.0793699, 
    viewOffsetY=0.000234077)
p1 = mdb.models['NACA4424_Airfoil2'].parts['MATLAB_MESH']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.95334, 
    farPlane=2.16168, width=1.27677, height=0.738313, viewOffsetX=0.12365, 
    viewOffsetY=-0.0144138)
p1 = mdb.models['NACA4424_Airfoil2'].parts['plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p1 = mdb.models['NACA4424_Airfoil2'].parts['MATLAB_MESH']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.84885, 
    farPlane=2.26618, width=2.54962, height=1.47436, viewOffsetX=0.721256, 
    viewOffsetY=0.00215185)
p1 = mdb.models['NACA4424_Airfoil2'].parts['plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
del mdb.models['NACA4424_Airfoil2'].parts['plate']
p = mdb.models['NACA4424_Airfoil2'].parts['MATLAB_MESH']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
s = mdb.models['NACA4424_Airfoil2'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.rectangle(point1=(-0.5, -0.5), point2=(1.5, 0.5))
session.viewports['Viewport: 1'].view.setValues(nearPlane=187.915, 
    farPlane=189.209, width=7.02834, height=4.06424, cameraPosition=(0.106682, 
    0.501439, 188.562), cameraTarget=(0.106682, 0.501439, 0))
s.Line(point1=(1.0, 0.0), point2=(0.95196, 0.0224))
s.Line(point1=(0.95196, 0.0224), point2=(0.9032, 0.04099))
s.Line(point1=(0.9032, 0.04099), point2=(0.80464, 0.07447))
s.Line(point1=(0.80464, 0.07447), point2=(0.70487, 0.10312))
s.Line(point1=(0.70487, 0.10312), point2=(0.60405, 0.12674))
s.Line(point1=(0.60405, 0.12674), point2=(0.50235, 0.14474))
s.Line(point1=(0.50235, 0.14474), point2=(0.4, 0.15606))
s.Line(point1=(0.4, 0.15606), point2=(0.29401, 0.15738))
s.Line(point1=(0.29401, 0.15738), point2=(0.24111, 0.15287))
s.Line(point1=(0.24111, 0.15287), point2=(0.18858, 0.14416))
s.Line(point1=(0.18858, 0.14416), point2=(0.13674, 0.13045))
s.Line(point1=(0.13674, 0.13045), point2=(0.08611, 0.11012))
s.Line(point1=(0.08611, 0.11012), point2=(0.06153, 0.09651))
s.Line(point1=(0.06153, 0.09651), point2=(0.03775, 0.07942))
s.Line(point1=(0.03775, 0.07942), point2=(0.01536, 0.05624))
s.Line(point1=(0.01536, 0.05624), point2=(0.0053, 0.03964))
s.Line(point1=(0.0053, 0.03964), point2=(0.0, 0.0))
s.Line(point1=(0.0, 0.0), point2=(0.0197, -0.03472))
s.Line(point1=(0.0197, -0.03472), point2=(0.03464, -0.04656))
s.Line(point1=(0.03464, -0.04656), point2=(0.06225, -0.06066))
s.Line(point1=(0.06225, -0.06066), point2=(0.08847, -0.06931))
s.Line(point1=(0.08847, -0.06931), point2=(0.11389, -0.07512))
s.Line(point1=(0.11389, -0.07512), point2=(0.16326, -0.08169))
s.Line(point1=(0.16326, -0.08169), point2=(0.21142, -0.08416))
s.Line(point1=(0.21142, -0.08416), point2=(0.25889, -0.08411))
s.Line(point1=(0.25889, -0.08411), point2=(0.30599, -0.08238))
s.Line(point1=(0.30599, -0.08238), point2=(0.4, -0.07606))
s.Line(point1=(0.4, -0.07606), point2=(0.49765, -0.06698))
s.Line(point1=(0.49765, -0.06698), point2=(0.59595, -0.05562))
s.Line(point1=(0.59595, -0.05562), point2=(0.69513, -0.04312))
s.Line(point1=(0.69513, -0.04312), point2=(0.79536, -0.03003))
s.Line(point1=(0.79536, -0.03003), point2=(0.8968, -0.01655))
s.Line(point1=(0.8968, -0.01655), point2=(0.94804, -0.00964))
s.Line(point1=(0.94804, -0.00964), point2=(1.0, 0.0))
p = mdb.models['NACA4424_Airfoil2'].Part(name='Plate', 
    dimensionality=TWO_D_PLANAR, type=DEFORMABLE_BODY)
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['NACA4424_Airfoil2'].sketches['__profile__']
session.viewports['Viewport: 1'].restore()
p1 = mdb.models['NACA4424_Airfoil2'].parts['MATLAB_MESH']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
del mdb.models['NACA4424_Airfoil2'].parts['MATLAB_MESH']
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['NACA4424_Airfoil2'].Material(name='plate')
mdb.models['NACA4424_Airfoil2'].materials['plate'].Elastic(table=((
    200000000000.0, 0.3), ))
mdb.models['NACA4424_Airfoil2'].HomogeneousSolidSection(name='platesection', 
    material='plate', thickness=None)
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(faces=faces, name='Set-1')
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
p.SectionAssignment(region=region, sectionName='platesection', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
a = mdb.models['NACA4424_Airfoil2'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['NACA4424_Airfoil2'].rootAssembly
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
a.Instance(name='Plate-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['NACA4424_Airfoil2'].StaticStep(name='Step-1', previous='Initial', 
    description='airfoil')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
p1 = mdb.models['NACA4424_Airfoil2'].parts['Plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
p.setMeshControls(regions=pickedRegions, elemShape=TRI)
elemType1 = mesh.ElemType(elemCode=CPS4R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=CPS3, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, distortionControl=DEFAULT)
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
pickedRegions =(faces, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
p.seedPart(size=2.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
p.seedPart(size=0.1, deviationFactor=0.1, minSizeFactor=0.1)
a = mdb.models['NACA4424_Airfoil2'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='coarse', model='NACA4424_Airfoil2', description='coarse mesh', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numCpus=1, numGPUs=0)
p1 = mdb.models['NACA4424_Airfoil2'].parts['Plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
elemType1 = mesh.ElemType(elemCode=CPS4R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=CPS3, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, distortionControl=DEFAULT)
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
pickedRegions =(faces, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
a = mdb.models['NACA4424_Airfoil2'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p1 = mdb.models['NACA4424_Airfoil2'].parts['Plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
a = mdb.models['NACA4424_Airfoil2'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
del mdb.jobs['coarse']
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p1 = mdb.models['NACA4424_Airfoil2'].parts['Plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
f, e, d1 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f[0], sketchPlaneSide=SIDE1, origin=(
    0.507154, -0.002855, 0.0))
s1 = mdb.models['NACA4424_Airfoil2'].ConstrainedSketch(name='__profile__', 
    sheetSize=4.47, gridSpacing=0.11, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
s1.unsetPrimaryObject()
del mdb.models['NACA4424_Airfoil2'].sketches['__profile__']
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
p.generateMesh()
elemType1 = mesh.ElemType(elemCode=CPS4R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=CPS3, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, distortionControl=DEFAULT)
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
pickedRegions =(faces, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.24958, 
    farPlane=4.69469, width=2.12287, height=1.44366, viewOffsetX=0.0390139, 
    viewOffsetY=0.0152984)
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
p.deleteMesh(regions=pickedRegions)
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
f1, e1, d2 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f1[0], sketchPlaneSide=SIDE1, origin=(
    0.507154, -0.002855, 0.0))
s = mdb.models['NACA4424_Airfoil2'].ConstrainedSketch(name='__profile__', 
    sheetSize=4.47, gridSpacing=0.11, transform=t)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.25263, 
    farPlane=4.69164, cameraPosition=(0.500093, 0.000671197, 4.47214), 
    cameraTarget=(0.500093, 0.000671197, 0))
s.Line(point1=(-1.5, 0.0), point2=(1.5, 0.0))
s.HorizontalConstraint(entity=g[40], addUndoState=False)
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
e, d1 = p.edges, p.datums
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s)
s.unsetPrimaryObject()
del mdb.models['NACA4424_Airfoil2'].sketches['__profile__']
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
p.seedPart(size=0.5, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
p.setMeshControls(regions=pickedRegions, technique=STRUCTURED)
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#2 ]', ), )
p.setMeshControls(regions=pickedRegions, technique=STRUCTURED)
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
p.generateMesh()
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#2 ]', ), )
p.deleteMesh(regions=pickedRegions)
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#2 ]', ), )
p.setMeshControls(regions=pickedRegions, technique=FREE)
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
p.generateMesh()
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
p.deleteMesh(regions=pickedRegions)
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
p.setMeshControls(regions=pickedRegions, technique=FREE)
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
p.generateMesh()
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
p.deleteMesh()
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
p.seedPart(size=0.055, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
p.generateMesh()
a = mdb.models['NACA4424_Airfoil2'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.saveAs(pathName='C:/temp/Coarse_mesh')
#: The model database has been saved to "C:\temp\Coarse_mesh.cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.Job(name='Job-1', model='NACA4424_Airfoil2', description='coarse_mesh', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numCpus=1, numGPUs=0)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Job Job-1: Abaqus/Standard completed successfully.
#: Job Job-1 completed successfully. 
p1 = mdb.models['NACA4424_Airfoil2'].parts['Plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
p.deleteMesh()
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
p.seedPart(size=0.07, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
p.generateMesh()
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.24938, 
    farPlane=4.6949, width=2.12509, height=1.44517, viewOffsetX=0.0773777, 
    viewOffsetY=0.0499124)
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
del p.features['Partition face-1']
#: Warning: Failed to attach mesh to part geometry.
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
p.generateMesh()
a = mdb.models['NACA4424_Airfoil2'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.Job(name='COARSEE', model='NACA4424_Airfoil2', description='COARSEE', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numCpus=1, numGPUs=0)
mdb.jobs['COARSEE'].submit(consistencyChecking=OFF)
#: The job input file "COARSEE.inp" has been submitted for analysis.
#: Job COARSEE: Analysis Input File Processor completed successfully.
#: Job COARSEE: Abaqus/Standard completed successfully.
#: Job COARSEE completed successfully. 
p1 = mdb.models['NACA4424_Airfoil2'].parts['Plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
p.deleteMesh()
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
p.seedPart(size=0.055, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['NACA4424_Airfoil2'].parts['Plate']
p.generateMesh()
a = mdb.models['NACA4424_Airfoil2'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.Job(name='fine_mesh_1500', model='NACA4424_Airfoil2', description='finee', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numCpus=1, numGPUs=0)
mdb.jobs['fine_mesh_1500'].submit(consistencyChecking=OFF)
#: The job input file "fine_mesh_1500.inp" has been submitted for analysis.
#: Job fine_mesh_1500: Analysis Input File Processor completed successfully.
#: Job fine_mesh_1500: Abaqus/Standard completed successfully.
#: Job fine_mesh_1500 completed successfully. 
mdb.save()
#: The model database has been saved to "C:\temp\Coarse_mesh.cae".
