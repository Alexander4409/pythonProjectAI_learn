import math

from ИИ_71_кем.Lesson_12 import outer


class Neuron:
    def __init__(self):
        self.w1 = 0.5
        self.w2 = 0.5
        self.bias = 0.0
        self.learn = 0.1

    def sigmoid(self,x):
        return 1/(1+math.exp(-x))

    def sigmoid_derivative(self,x):
        fx = self.sigmoid(x)
        return fx *(1 - fx)

    def forward(self,x1, x2):
        self.last_x1 = x1
        self.last_x2 = x2
        self.raw_sum = (x1 * self.w1) + (x2 * self.w2) + self.bias
        return self.sigmoid(self.raw_sum)

    def train(self, target, y_pred):

        error = target - y_pred

        delta = error * self.sigmoid_derivative(self.raw_sum)

        self.w1 += self.learn * delta * self.last_x1
        self.w2 += self.learn * delta * self.last_x2
        self.bias += self.learn * delta

# данные для обучения
training_data = [(0,0,0),
                 (0,1,0),
                 (1,0,0),
                 (1,1,1)]



#__пример использования__

neuron = Neuron()

print("Start learn")
for epoch in range(200000):
    for x1, x2, target in training_data:
        y_pred = neuron.forward(x1, x2)
        neuron.train(target,y_pred)

print("Learn compete")

# объединение в сеть

#тестирование нейрона
print("Check results")

for x1, x2, target in training_data:
    output = neuron.forward(x1,x2)
    final_res = 1 if output > 0.5 else 0
    print(f"Exits {x1}, {x2}, Predict - {output:.4f} -> answer {final_res}, Expect :{target}")



# 0 and 0 = 0
# 0 and 1 = 0
# 1 and 0 = 0
# 1 and 1 = 1
