from glob import glob
import tensorflow as tf

glob('dataset-clean,dirty.zip')

!mkdir IMAGE
!cp ./dataset-clean,dirty.zip ./IMAGE
!cd IMAGE ; unzip -o dataset-clean,dirty.zip
!ls -l ./IMAGE/dataset-clean,dirty/clean | grep jpg | wc -l
!ls -l ./IMAGE/dataset-clean,dirty/dirty | grep jpg | wc -l