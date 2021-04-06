print("____________________________________________________________________________________\n")


print("                        Dyhibrid Punnet Square Calculator\n")


print("_____________________________________PARENT 1_______________________________________\n")


choice1 = input("PARENT ALLELE 1(A/a)")

A = "A"

a = "a"

B = "B"

b = "b"

# Parent 1

if choice1 == 'A':
    X = A


elif choice1 == 'a':
    X = a

choice2 = input("PARENT ALLELE 2(A/a)")


if choice2 == 'A':
    Y = A


elif choice2 == 'a':
    Y = a
# -

choice3 = input("PARENT ALLELE 3(B/b)")

if choice3 == 'B':
    Z = B


elif choice3 == 'b':
    Z = b

choice4 = input("PARENT ALLELE 4(B/b)")

if choice4 == 'B':
    Q = B


elif choice4 == 'b':
    Q = b


print("_____________________________________PARENT 2_______________________________________\n")


# Parent 2
choice5 = input("PARENT ALLELE 5(A/a)")


if choice5 == 'A':
    H = A


elif choice5 == 'a':
    H = a

choice6 = input("PARENT ALLELE 6(A/a)")


if choice6 == 'A':
    J = A


elif choice6 == 'a':
    J = a

# -

choice7 = input("PARENT ALLELE 7(B/b)")

if choice7 == 'B':
    K = B


elif choice7 == 'b':
    K = b

choice8 = input("PARENT ALLELE 8(B/b)")

if choice8 == 'B':
    L = B


elif choice8 == 'b':
    L = b

# -

print("___________________________________________________________________________________\n")

print("PARENT 1 =", (X, Y), (Z, Q))

print("PARENT 2 =", (H, J), (K, L))


print("____________________________________________________________________________________")

Delta1 = (H, X, K, Z), (H, X, Z, L), (X, J, Z, K), (X, J, Z, L)

print(*Delta1)

Delta2 = (H, X, K, Q), (H, X, Q, L), (X, J, K, L), (X, J, L, Q)

print(*Delta2)

Delta3 = (H, Y, Z, K), (H, Y, Z, L), (J, Y, Z, K), (J, Y, Z, L)

print(*Delta3)

Delta4 = (H, Y, K, Q), (H, Y, Q, L), (J, Y, K, Q), (J, Y, Q, L)

print(*Delta4)
print("____________________________________________________________________________________")


# Count Genotypes


E = (['A', 'A', 'B', 'B'])

E2 = (['A', 'A', 'B', 'b'])

E3 = (['A', 'A', 'b', 'b'])

E4 = (['A', 'a', 'B', 'B'])

E5 = (['A', 'a', 'B', 'b'])

E6 = (['A', 'a', 'b', 'b'])

E7 = (['a', 'a', 'B', 'B'])

E8 = (['a', 'a', 'B', 'b'])

E9 = (['a', 'a', 'b', 'b'])


# --------------------------------------------------------- 1


listDELTA1 = (([H, X, K, Z]), ([H, X, Z, L]), ([X, J, Z, K]), ([X, J, Z, L]))
elm_count1 = listDELTA1.count(E)

listDELTA2 = (([H, X, K, Q]), ([H, X, Q, L]), ([X, J, K, L]), ([X, J, L, Q]))
elm_count2 = listDELTA2.count(E)

listDELTA3 = (([H, Y, Z, K]), ([H, Y, Z, L]), ([J, Y, Z, K]), ([J, Y, Z, L]))
elm_count3 = listDELTA3.count(E)

listDELTA4 = (([H, Y, K, Q]), ([H, Y, Q, L]), ([J, Y, K, Q]), ([J, Y, Q, L]))
elm_count4 = listDELTA4.count(E)


q1 = (elm_count1+elm_count2+elm_count3+elm_count4)


# ----------------------------------------------------------- 2

elm_count12 = listDELTA1.count(E2)

elm_count22 = listDELTA2.count(E2)

elm_count32 = listDELTA3.count(E2)

elm_count42 = listDELTA4.count(E2)

q2 = (elm_count12 + elm_count22 + elm_count32 + elm_count42)

# ------------------------------------------------------------ 3

elm_count13 = listDELTA1.count(E3)

elm_count23 = listDELTA2.count(E3)

elm_count33 = listDELTA3.count(E3)

elm_count43 = listDELTA4.count(E3)

q3 = (elm_count13 + elm_count23 + elm_count33 + elm_count43)

# ------------------------------------------------------------ 4


elm_count14 = listDELTA1.count(E4)

elm_count24 = listDELTA2.count(E4)

elm_count34 = listDELTA3.count(E4)

elm_count44 = listDELTA4.count(E4)

q4 = (elm_count14 + elm_count24 + elm_count34 + elm_count44)


# ----------------------------------------------------------- 5

elm_count15 = listDELTA1.count(E5)

elm_count25 = listDELTA2.count(E5)

elm_count35 = listDELTA3.count(E5)

elm_count45 = listDELTA4.count(E5)

q5 = (elm_count15 + elm_count25 + elm_count35 + elm_count45)


# ----------------------------------------------------------- 6

elm_count16 = listDELTA1.count(E6)

elm_count26 = listDELTA2.count(E6)

elm_count36 = listDELTA3.count(E6)

elm_count46 = listDELTA4.count(E6)

q6 = (elm_count16 + elm_count26 + elm_count36 + elm_count46)

# ------------------------------------------------------------ 7

elm_count17 = listDELTA1.count(E7)

elm_count27 = listDELTA2.count(E7)

elm_count37 = listDELTA3.count(E7)

elm_count47 = listDELTA4.count(E7)

q7 = (elm_count17 + elm_count27 + elm_count37 + elm_count47)

# ------------------------------------------------------------ 8

elm_count18 = listDELTA1.count(E8)

elm_count28 = listDELTA2.count(E8)

elm_count38 = listDELTA3.count(E8)

elm_count48 = listDELTA4.count(E8)

q8 = (elm_count18 + elm_count28 + elm_count38 + elm_count48)

# -----------------------------------------------------------  9

elm_count19 = listDELTA1.count(E9)

elm_count29 = listDELTA2.count(E9)

elm_count39 = listDELTA3.count(E9)

elm_count49 = listDELTA4.count(E9)

q9 = (elm_count19 + elm_count29 + elm_count39 + elm_count49)

# BOTH A / B
S1 = (q1 + q2 + q4 + q5)
# BOTH A / b
S2 = (q3 + q6)
# BOTH a / B
S3 = (q7 + q8)
# BOTH a / b
S4 = q9


print("                " "A/B A/b a/B a/b")
print("Dyhibrid ratio =", S1, S2, S3, S4)


print("____________________________________________________________________________________\n")

T = (q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8 + q9)

F1 = (q1/T)
print(q1, "=", "AABB", F1*100, "%")

F2 = (q2/T)
print(q2, "=", "AABb", F2*100, "%")

F3 = (q3/T)
print(q3, "=", "AAbb", F3*100, "%")

F4 = (q4/T)
print(q4, "=", "AaBB", F4*100, "%")

F5 = (q5/T)
print(q5, "=", "AaBb", F5*100, "%")

F6 = (q6/T)
print(q6, "=", "Aabb", F6*100, "%")

F7 = (q7/T)
print(q7, "=", "aaBB", F7*100, "%")

F8 = (q8/T)
print(q8, "=", "aaBb", F8*100, "%")

F9 = (q9/T)
print(q9, "=", "aabb", F9*100, "%")
