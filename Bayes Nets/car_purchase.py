from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = BayesianNetwork([
    ('B', 'I'),
    ('M', 'I'),
    ('I', 'R'),
    ('I', 'T'),
    ('R', 'C'),
    ('T', 'C'),
    ('D', 'C')
])


cpd_B = TabularCPD('B', 2, [[0.65], [0.35]])
cpd_M = TabularCPD('M', 2, [[0.55], [0.45]])
cpd_D = TabularCPD('D', 2, [[0.75], [0.25]])


cpd_I = TabularCPD('I', 2,
                   [[0.88, 0.35, 0.28, 0.07],
                    [0.12, 0.65, 0.72, 0.93]],
                   evidence=['B', 'M'],
                   evidence_card=[2, 2])


cpd_R = TabularCPD('R', 2,
                   [[0.80, 0.20],
                    [0.20, 0.80]],
                   evidence=['I'],
                   evidence_card=[2])


cpd_T = TabularCPD('T', 2,
                   [[0.70, 0.15],
                    [0.30, 0.85]],
                   evidence=['I'],
                   evidence_card=[2])

cpd_C = TabularCPD('C', 2,
                   [[0.96, 0.68, 0.52, 0.25,
                     0.45, 0.22, 0.12, 0.03],
                    [0.04, 0.32, 0.48, 0.75,
                     0.55, 0.78, 0.88, 0.97]],
                   evidence=['R', 'T', 'D'],
                   evidence_card=[2, 2, 2])

model.add_cpds(cpd_B, cpd_M, cpd_D, cpd_I, cpd_R, cpd_T, cpd_C)


print("Model valid:", model.check_model())


infer = VariableElimination(model)

print("\n1. P(I=1 | B=1, M=1):")
print(infer.query(['I'], evidence={'B': 1, 'M': 1}))

print("\n2. P(R=1 | I=1):")
print(infer.query(['R'], evidence={'I': 1}))

print("\n3. P(C=1 | T=1):")
print(infer.query(['C'], evidence={'T': 1}))

print("\n4. P(B=1 | I=1):")
print(infer.query(['B'], evidence={'I': 1}))

print("\n5. P(M=1 | I=1):")
print(infer.query(['M'], evidence={'I': 1}))

print("\n6. P(T=1 | C=1, R=0):")
print(infer.query(['T'], evidence={'C': 1, 'R': 0}))