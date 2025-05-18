import sys
sys.path.append("/home/shashank/anomalib/src/")

import warnings
warnings.filterwarnings("ignore")


from anomalib.data import MVTecAD
from anomalib.models import Padim
from anomalib.engine import Engine
from anomalib.visualization import ImageVisualizer

categories = [ 
              'bottle', 'cable', 'capsule', 'carpet',
              'grid', 'hazelnut', 'leather', 'metal_nut',
              'pill', 
              'screw',  'tile', 'toothbrush',
              'transistor',  'wood',  'zipper'
              ]

output_dir = "/home/shashank/repos/image_anamoly_detection/PaDiM/results"
root = "/home/shashank/tensorflow_datasets/downloads/mvtecad"


for category in categories:

    # Initialize components
    datamodule = MVTecAD(root=root, category=category)

    image_visualizer = ImageVisualizer(output_dir=output_dir)
    model = Padim(visualizer=image_visualizer)
    engine = Engine()

    # Train the model
    engine.fit(datamodule=datamodule, model=model)
    
    # Evaluate the model
    engine.test(datamodule=datamodule, model=model)