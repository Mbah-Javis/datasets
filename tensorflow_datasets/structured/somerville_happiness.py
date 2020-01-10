

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets.public_api as tfds

_CITATION = """
@misc{Waldemar:2020 ,
author = "Waldemar W. Koczkodaj",
year = "2015",
title = "{UCI} Machine Learning Repository",
url = "http://archive.ics.uci.edu/ml",
institution = "University of California, Irvine, School of Information and Computer Sciences"
}
"""

_DESCRIPTION = """It is a case of supervised learning with the use of Receiver Operating Characteristic (ROC) to 
select the minimal set of attributes preserving or increasing predictability of the data.

Attribute Information:

D = decision attribute (D) with values 0 (unhappy) and 1 (happy) 
X1 = the availability of information about the city services 
X2 = the cost of housing 
X3 = the overall quality of public schools 
X4 = your trust in the local police 
X5 = the maintenance of streets and sidewalks 
X6 = the availability of social community events 

Attributes X1 to X6 have values 1 to 5.
"""

_URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00479/SomervilleHappinessSurvey2015.csv'

class SomervilleHappiness(tfds.core.GeneratorBasedBuilder):
  
  
  VERSION = tfds.core.Version('2.0.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        
        features=tfds.features.FeaturesDict({
           "D": tfds.features.ClassLabel(num_classes=2),
           "X1": tfds.features.ClassLabel(num_classes=5),
           "X2": tfds.features.ClassLabel(num_classes=5),
           "X3": tfds.features.ClassLabel(num_classes=5),
           "X4": tfds.features.ClassLabel(num_classes=5),
           "X5": tfds.features.ClassLabel(num_classes=5),
           "X6": tfds.features.ClassLabel(num_classes=5),
        }),
        supervised_keys=('D', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6'),
        homepage='https://archive.ics.uci.edu/ml/datasets/Somerville+Happiness+Survey',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    path = dl_manager.download_and_extract(_URL)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
              'file_path': path,
            },
        ),
    ]

  def _generate_examples(self, file_path):
    fieldname = ['D, X1, X2, X3, X4, X5, X6']
    with tf.io.gfile.GFile(file_path) as csvfile:
      reader = csv.DictReader(csvfile, fieldnames=fieldname)
      for i, row in enumerate(reader):
        yield i, row


