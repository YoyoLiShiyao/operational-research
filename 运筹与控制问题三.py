#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np

def simulate_duel(num_simulations):
    jack_survivals = 0
    john_survivals = 0
    carter_survivals = 0

    for _ in range(num_simulations):
        jack, john, carter = True, True, True

        while sum([jack, john, carter]) > 1:  # 当超过一个存活
            if jack and john and carter:
                # 都存活： 杰克射约翰, 约翰和卡特射杰克
                if np.random.rand() < 0.8:
                    john = False  # 杰克击中约翰
                if np.random.rand() < 0.6 or np.random.rand() < 0.4:
                    jack = False  # 约翰或卡特击中杰克
            elif jack and john:
                # 杰克vs约翰
                if np.random.rand() < 0.8:
                    john = False  # 杰克击中约翰
                if np.random.rand() < 0.6:
                    jack = False  #约翰击中杰克
            elif jack and carter:
                # Jack vs Carter
                if np.random.rand() < 0.8:
                    carter = False  # 杰克击中卡特
                if np.random.rand() < 0.4:
                    jack = False  # 卡特击中杰克
            elif john and carter:
                # John vs Carter
                if np.random.rand() < 0.6:
                    carter = False  # 约翰击中卡特
                if np.random.rand() < 0.4:
                    john = False  # 卡特击中约翰

        # 计算存活率
        if jack:
            jack_survivals += 1
        if john:
            john_survivals += 1
        if carter:
            carter_survivals += 1

    return {
        "Jack": jack_survivals / num_simulations,
        "John": john_survivals / num_simulations,
        "Carter": carter_survivals / num_simulations
    }

#运行100,000次
results = simulate_duel(100000)
print(results)


# In[ ]:




