# -*- coding: utf-8 -*-
# @author: Spark
# @file: basics.py
# @ide: PyCharm
# @time: 2020-01-14 10:30:39

import tensorflow as tf

# # 定义一个随机数（标量）
# random_float = tf.random.uniform(shape=())
# print(random_float)
#
# # 定义一个有2个元素的零向量
# zero_vector = tf.zeros(shape=(10,))
# print(zero_vector)
#
# # 定义两个2×2的常量矩阵
# A = tf.constant([[1., 2.], [3., 4.]])
# B = tf.constant([[5., 6.], [7., 8.]])
#
# print(tf.add(A, B))  # 矩阵相加
# print(tf.matmul(A, B))   # 矩阵相乘
#
# x = tf.Variable(initial_value=5.)
# a = tf.Variable(initial_value=[5, 10, 15])
# print(x)
# with tf.GradientTape() as tape:     # 在 tf.GradientTape() 的上下文内，所有计算步骤都会被记录以用于求导
#     y = tf.square(x) + 10*x + 5
#
# y_grad = tape.gradient(y, x)        # 计算y关于x的导数
# print([y, y_grad])

# X = tf.constant([[1., 2.], [3., 4.]])
# y = tf.constant([[1.], [2.]])
# w = tf.Variable(initial_value=[[1.], [2.]])
# b = tf.Variable(initial_value=1.)
# with tf.GradientTape() as tape:
#     L = 0.5 * tf.reduce_sum(tf.square(tf.matmul(X, w) + b - y))
# w_grad, b_grad = tape.gradient(L, [w, b])        # 计算L(w, b)关于w, b的偏导数
# print([L.numpy(), w_grad.numpy(), b_grad.numpy()])

# import numpy as np
#
# X_raw = np.array([2013, 2014, 2015, 2016, 2017], dtype=np.float32)
# y_raw = np.array([12000, 14000, 15000, 16500, 17500], dtype=np.float32)
#
# X = (X_raw - X_raw.min()) / (X_raw.max() - X_raw.min())
# y = (y_raw - y_raw.min()) / (y_raw.max() - y_raw.min())
# # print(X, y)
#
# X = tf.constant(X)
# y = tf.constant(y)
#
# a = tf.Variable(initial_value=0.)
# b = tf.Variable(initial_value=0.)
# variables = [a, b]
#
# num_epoch = 10000
# optimizer = tf.keras.optimizers.SGD(learning_rate=1e-3)
# for e in range(num_epoch):
#     # 使用tf.GradientTape()记录损失函数的梯度信息
#     with tf.GradientTape() as tape:
#         y_pred = a * X + b
#         loss = 0.5 * tf.reduce_sum(tf.square(y_pred - y))
#     # TensorFlow自动计算损失函数关于自变量（模型参数）的梯度
#     grads = tape.gradient(loss, variables)
#     # TensorFlow自动根据梯度更新参数
#     optimizer.apply_gradients(grads_and_vars=zip(grads, variables))
#     print(e)
#
# print(a, b)

import tensorflow as tf

X = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
y = tf.constant([[10.0], [20.0]])


class Linear(tf.keras.Model):
    def __init__(self):
        super().__init__()
        self.dense = tf.keras.layers.Dense(
            units=1,
            activation=None,
            kernel_initializer=tf.zeros_initializer(),
            bias_initializer=tf.zeros_initializer()
        )

    def call(self, x_input):
        output = self.dense(x_input)
        return output


# 以下代码结构与前节类似
model = Linear()
optimizer = tf.keras.optimizers.SGD(learning_rate=0.01)
for i in range(800):
    with tf.GradientTape() as tape:
        y_pred = model(X)      # 调用模型 y_pred = model(X) 而不是显式写出 y_pred = a * X + b
        loss = tf.reduce_mean(tf.square(y_pred - y))
    grads = tape.gradient(loss, model.variables)    # 使用 model.variables 这一属性直接获得模型中的所有变量
    optimizer.apply_gradients(grads_and_vars=zip(grads, model.variables))
print(model.variables)

