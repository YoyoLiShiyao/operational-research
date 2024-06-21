#!/usr/bin/env python
# coding: utf-8

# In[8]:


from ortools.linear_solver import pywraplp

def solve_with_or_tools(prices, weights, limits, min_price, max_price, min_weight):
    # 创建求解器实例
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # 决策变量
    x = [solver.IntVar(0, limits[i], f'x[{i}]') for i in range(len(prices))]

    # 目标函数
    objective = solver.Objective()
    for i in range(len(prices)):
        objective.SetCoefficient(x[i], prices[i])
    objective.SetMinimization()

    # 约束条件
    # 价格约束
    price_constraint = solver.Constraint(min_price, max_price)
    for i in range(len(prices)):
        price_constraint.SetCoefficient(x[i], prices[i])

    # 重量约束
    weight_constraint = solver.Constraint(min_weight, solver.infinity())
    for i in range(len(weights)):
        weight_constraint.SetCoefficient(x[i], weights[i])

    # 求解问题
    status = solver.Solve()

    # 输出结果
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Objective value =', solver.Objective().Value())
        for i in range(len(x)):
            if x[i].solution_value() > 0:
                print(f'x[{i}] = {x[i].solution_value()}')
    else:
        print('The problem does not have an optimal solution.')

# 定义数据
prices = [0.2, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.2, 6, 7.2, 10.8, 12.8, 18.8, 20.8, 24.88, 30.88, 38.88, 42, 52, 66.66]
weights = [0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 4, 5, 5, 6, 8, 10, 10, 12, 15, 22]
limits = [5, 2, 2, 3, 3, 5, 5, 5, 6, 10, 10, 8, 8, 8, 8, 6, 6, 3, 3, 1, 1, 1]

# 解决问题一
print("Problem 1:")
solve_with_or_tools(prices, weights, limits, 80, 140, 30)

# 解决问题二
print("\nProblem 2:")
solve_with_or_tools(prices, weights, limits, 150, 300, 60)


# In[ ]:





# In[ ]:




