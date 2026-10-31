import random
import math


random.seed(42)

class XORNetwork:
    def __init__(self):
        self.lr_speed = 0.2
        # скрытый слой h1
        self.w11 = random.uniform(-1,1)
        self.w12 = random.uniform(-1,1)
        self.b1 = random.uniform(-1,1)
        # скрытый слой h2
        self.w21 = random.uniform(-1, 1)
        self.w22 = random.uniform(-1, 1)
        self.b2 = random.uniform(-1, 1)

        self.w_out_1 = random.uniform(-1,1)
        self.w_out_2 = random.uniform(-1,1)
        self.b_out = random.uniform(-1,1)

    def sigmoid(self,x):
        return 1/(1+math.exp(-x))

    def sigmoid_derivative(self,x):
        return x *(1 - x)

    def forward(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
        # считаем скрытые слой
        self.h1_input = (x1 * self.w11) + (x2 * self.w12)
        self.h1_out = self.sigmoid(self.h1_input)

        self.h2_input = (x1 * self.w21) + (x2 * self.w22)
        self.h2_out = self.sigmoid(self.h2_input)

        # считаем выходные слои
        self.out_input = (self.h1_out * self.w_out_1) + (self.h2_out*self.w_out_2)
        self.final_out = self.sigmoid(self.out_input)


        return self.final_out

    def train(self,target):

        #ошибка выходного слоя
        out_error = target - self.final_out
        out_delta = out_error * self.sigmoid_derivative(self.final_out)

        # ошибка на скрытых слоях

        h1_error = out_delta*self.w_out_1
        h1_delta = h1_error * self.sigmoid_derivative(self.h1_out)

        h2_error = out_delta*self.w_out_2
        h2_delta = h2_error*self.sigmoid_derivative(self.h2_out)

        # корректировка весов выходного слоя

        self.w_out_1 += self.lr_speed * out_delta * self.h1_out
        self.w_out_2 += self.lr_speed * out_delta * self.h2_out
        self.b_out += self.lr_speed * out_delta

        # корректировка скрытых слоев
        self.w11 += self.lr_speed * h1_delta * self.x1
        self.w12 += self.lr_speed * h1_delta * self.x2
        self.b1 += self.lr_speed * h1_delta

        self.w21 += self.lr_speed * h2_delta * self.x1
        self.w22 += self.lr_speed * h2_delta * self.x2
        self.b2 += self.lr_speed * h2_delta

xor_data_learn = [
    (0,0,0),
    (0,1,1),
    (1,0,1),
    (1,1,0)
]

network = XORNetwork()

print("Start network learn")

for epoc in range(60000):
    for x1, x2, target in xor_data_learn:
        network.forward(x1,x2)
        network.train(target)

print("Learn complete")

for x1, x2, target in xor_data_learn:
    output = network.forward(x1, x2)
    final_result = 1 if output > 0.5 else 0
    print(f"Exits - {x1}, {x2}| Prediction - {output:.4f}, Answer: {final_result}, Expect - {target}")