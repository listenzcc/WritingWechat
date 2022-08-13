## tensorflow-1to2

---

-   [tensorflow-1to2](#tensorflow-1to2)
-   [Migrate tensorflow 1 to 2](#migrate-tensorflow-1-to-2)
-   [Tensorflow compatibility](#tensorflow-compatibility)
-   [Tensorflow contrib](#tensorflow-contrib)
-   [Neuralgym](#neuralgym)

## Migrate tensorflow 1 to 2

It is how I migrate tensorflow scripts from version 1.x to 2.x. Specifically, I migrate the generative_inpainting project into tensorflow 2.x, which is originally released by supporting the tensorflow<=1.7.0, which is hard to operate with either new hardware and new software features.

## Tensorflow compatibility

The tensorflow provides compatibility with 1.x version, using the following replacement

```python
# Replace the original importimport tensorflow as tf# By the compatibility wayimport tensorflow.compat.v1 as tftf.disable_v2_behavior()  # noqa
```

## Tensorflow contrib

Replace the contrib methods one-by-one.

-   arg_scope

    ```python
    # from tensorflow.contrib.framework.python.ops import arg_scopefrom tf_slim import arg_scope
    ```

-   add_arg_score

    ```python
    # from tensorflow.contrib.framework.python.ops import add_arg_scopefrom tf_slim import add_arg_scope
    ```

-   framework.load_variable

    ```python
    # var_value = tf.contrib.framework.load_variable(var_value = tf.train.load_variable(    args.checkpoint_dir, from_name)
    ```

-   layers.xavier_initializer_conv2d

    ```python
    # w_init = tf.contrib.layers.xavier_initializer_conv2d()w_init=tf.keras.initializers.glorot_normal()
    ```

## Neuralgym

The neuralgym is the package being required by the generative_inpainting project. The package supports only the tensorflow 1.x too. So, basically, I migrate it with the methods that have been mentioned above.
