from glob import glob
import tensorflow as tf

clean_img_path = './IMAGE/dataset-clean,dirty/clean/plastic1.jpg'

gfile = tf.io.read_file(clean_img_path)
image = tf.io.decode_image(gfile, dtype=tf.float32)

image.shape

plt.imshow(image)
plt.show()

dirty_img_path = './IMAGE/dataset-clean,dirty/dirty/dirty_plastic1.jpg'

gfile = tf.io.read_file(dirty_img_path)
image = tf.io.decode_image(gfile, dtype=tf.float32)
image.shape
plt.imshow(image)
plt.show()