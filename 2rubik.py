"""print("請選擇一面輸入顏色(英文:w, o, g, r, b, y):")
side1 = [list(input().split()) for _ in range(2)]
print("由上往下轉一個面並輸入顏色:")
side2 = [list(input().split()) for _ in range(2)]
print("由左往右轉一個面並輸入顏色:")
side3 = [list(input().split()) for _ in range(2)]
print("由左往右轉一個面並輸入顏色:")
side4 = [list(input().split()) for _ in range(2)]
print("由左往右轉一個面並輸入顏色:")
side5 = [list(input().split()) for _ in range(2)]
print("由左往右轉一個面 再由上往下轉一個面並輸入顏色:")
side6 = [list(input().split()) for _ in range(2)]
print("以第1個輸入的面朝下 第2個輸入的面朝自己")"""
side1 = [["g","r"],["o","r"]]
side2 = [["w","g"],["o","b"]]
side3 = [["r","b"],["y","y"]]
side4 = [["y","w"],["g","w"]]
side5 = [["r","o"],["g","y"]]
side6 = [["b","o"],["b","w"]]
side = [side1,side2,side3,side4,side5,side6]
Uside = [side2, side3, side4, side5]
Fside = [side1, side3, side5, side6]
Rside = [side1, side2, side4, side6]
Dside = [side2, side3, side4, side5]

def reload():
   global Uside, Fside, Rside, side, Dside
   Uside = [side[1], side[2], side[3], side[4]]
   Fside = [side[0], side[2], side[4], side[5]]
   Rside = [side[0], side[1], side[3], side[5]]
   Dside = [side[1], side[2], side[3], side[4]]

def matrix_turn_left(matrix, n):  # 矩陣逆時針翻轉
   for i in range(n // 2):
       for j in range(i, n - i - 1):
           a = matrix[i][j]
           matrix[i][j] = matrix[j][n - i - 1]
           matrix[j][n - i - 1] = matrix[n - i - 1][n - j - 1]
           matrix[n - i - 1][n - j - 1] = matrix[n - j - 1][i]
           matrix[n - j - 1][i] = a

def matrix_turn_right(matrix, n):  # 矩陣順時針翻轉
   for i in range(n // 2):
       for j in range(i, n - i - 1):
           a = matrix[i][j]
           matrix[i][j] = matrix[n - 1 - j][i]
           matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
           matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
           matrix[j][n - 1 - i] = a

def U_r(Uside, side1, side6):  # Uside = [side2, side3, side4, side5]
   for i in range(2):
       a = Uside[0][0][i]
       Uside[0][0][i] = Uside[3][0][i]
       Uside[3][0][i] = Uside[2][0][i]
       Uside[2][0][i] = Uside[1][0][i]
       Uside[1][0][i] = a
   matrix_turn_left(side6, 2)

def U_l(Uside, side1, side6):  # Uside = [side2, side3, side4, side5]
   for i in range(2):
       a = Uside[0][0][i]
       Uside[0][0][i] = Uside[1][0][i]
       Uside[1][0][i] = Uside[2][0][i]
       Uside[2][0][i] = Uside[3][0][i]
       Uside[3][0][i] = a
   matrix_turn_right(side6, 2)

def F_r(Fside, side2, side4):  # Fside = [side1, side3, side5, side6]
   for i in range(2):
       a = Fside[3][1][i]  # 紀錄黃色
       Fside[3][1][i] = Fside[2][-i-1][1]  # 黃 = 紅
       Fside[2][-i-1][1] = Fside[0][0][-i-1]  # 紅 = 白
       Fside[0][0][-i-1] = Fside[1][i][0]  # 白 = 橘
       Fside[1][i][0] = a  # 橘 = 黃
   matrix_turn_right(side2, 2)

def F_l(Fside, side2, side4):  # Fside = [side1, side3, side5, side6]
   for i in range(2):
       a = Fside[3][1][i]
       Fside[3][1][i] = Fside[1][i][0]
       Fside[1][i][0] = Fside[0][0][-i-1]
       Fside[0][0][-i-1] = Fside[2][-i-1][1]
       Fside[2][-i-1][1] = a
   matrix_turn_left(side2, 2)

def R_r(Rside, side3, side5):
   for i in range(2):  # Rside = [side1, side2, side4, side6]
       a = Rside[3][i][1]
       Rside[3][i][1] = Rside[1][i][1]
       Rside[1][i][1] = Rside[0][i][1]
       Rside[0][i][1] = Rside[2][-i-1][0]
       Rside[2][-i-1][0] = a
   matrix_turn_right(side3, 2)

def R_l(Rside, side3, side5):
   for i in range(2):  # Rside = [side1, side2, side4, side6]
       a = Rside[3][i][1]
       Rside[3][i][1] = Rside[2][-i-1][0]
       Rside[2][-i-1][0] = Rside[0][i][1]
       Rside[0][i][1] = Rside[1][i][1]
       Rside[1][i][1] = a
   matrix_turn_left(side3, 2)

def U(Uside, side1, side6):
   U_l(Uside, side1, side6)
   side[0] = side1
   side[1] = Uside[0]
   side[2] = Uside[1]
   side[3] = Uside[2]
   side[4] = Uside[3]
   side[5] = side6
   reload()

def U_(Uside, side1, side6):
   U_r(Uside, side1, side6)
   side[0] = side1
   side[1] = Uside[0]
   side[2] = Uside[1]
   side[3] = Uside[2]
   side[4] = Uside[3]
   side[5] = side6
   reload()

def F(Fside, side2, side4):
   F_r(Fside, side2, side4)
   side[0] = Fside[0]
   side[1] = side2
   side[2] = Fside[1]
   side[3] = side4
   side[4] = Fside[2]
   side[5] = Fside[3]
   reload()

def F_(Fside, side2, side4):
   F_l(Fside, side2, side4)
   side[0] = Fside[0]
   side[1] = side2
   side[2] = Fside[1]
   side[3] = side4
   side[4] = Fside[2]
   side[5] = Fside[3]
   reload()

def R(Rside, side3, side5):
   R_r(Rside, side3, side5)
   side[0] = Rside[0]
   side[1] = Rside[1]
   side[2] = side3
   side[3] = Rside[2]
   side[4] = side5
   side[5] = Rside[3]
   reload()

def R_(Rside, side3, side5):
   R_l(Rside, side3, side5)
   side[0] = Rside[0]
   side[1] = Rside[1]
   side[2] = side3
   side[3] = Rside[2]
   side[4] = side5
   side[5] = Rside[3]
   reload()

def D_l(Dside, side1, side6):  # Dside = [side2, side3, side4, side5]
    for i in range(2):
        a = Dside[0][1][i]
        Dside[0][1][i] = Dside[3][1][i]
        Dside[3][1][i] = Dside[2][1][i]
        Dside[2][1][i] = Dside[1][1][i]
        Dside[1][1][i] = a
    matrix_turn_right(side1, 2)  # 修正為對底面進行旋轉

def D(Dside, side1, side6):
    D_l(Dside, side1, side6)
    side[0] = side1
    side[1] = Dside[0]
    side[2] = Dside[1]
    side[3] = Dside[2]
    side[4] = Dside[3]
    side[5] = side6
    reload()

def D_(Dside, side1, side6):
   for i in range(3):
      D(Dside, side1, side6)

def print_cube(side):  # print each side
   for i, j in enumerate(side, start=1):
       print(f"Side {i}:")
       for row in j:
           print(" ".join(row))
       print()

# Test the function
print("一開始的魔方")
print_cube(side)

def step1(side):
   side1 = side[0];side2 = side[1];side3 = side[2];side4 = side[3];side5 = side[4];side6 = side[5]
   reload()
   for i in range(4):
      if side[0][0][0] != "w":
         for i in range(4):
            if side2[0][0] == "w":
               F(Fside, side2, side4)
               U(Uside, side1, side6)
               F_(Fside, side2, side4)
               print("F U F'")
            elif side2[0][1] == "w":
               U(Uside, side1, side6)
               U(Uside, side1, side6)
               F(Fside, side2, side4)
               U_(Uside, side1, side6)
               F_(Fside, side2, side4)
               print("U2 F U' F'")
            elif side6[1][1] == "w":
               R(Rside, side3, side5)
               U(Uside, side1, side6)
               U(Uside, side1, side6)
               R_(Rside, side3, side5)
               F(Fside, side2, side4)
               U(Uside, side1, side6)
               F_(Fside, side2, side4)
               U(Uside, side1, side6)
               U(Uside, side1, side6)
               R(Rside, side3, side5)
               U_(Uside, side1, side6)
               R_(Rside, side3, side5)
               print("R U2 R' F U F' U2 R U' R'")
            elif side2[1][0] == "w":
               F(Fside, side2, side4)
               U(Uside, side1, side6)
               F_(Fside, side2, side4)
               U_(Uside, side1, side6)
               F(Fside, side2, side4)
               U(Uside, side1, side6)
               F_(Fside, side2, side4)
               print("F U F' U' F U F'")
            else:
               U(Uside, side1, side6)
               print("U")
            if side[0][0][0] == "w" and side[0][0][1] == "w" and side[0][1][0] == "w" and side[0][1][1] == "w": break
      D(Dside, side1, side6)
      print("D")
def step2(side):
   side1 = side[0];side2 = side[1];side3 = side[2];side4 = side[3];side5 = side[4];side6 = side[5]
   reload()
   for i in range(4):
      if side6 == [["y", "y"],["y", "y"]]: break
      if side6[0][0] == "y" and side2[0][0] == "y" and side3[0][0] == "y" and side4[0][0] == "y":
         R_(Rside, side3, side5)
         U_(Uside, side1, side6)
         R(Rside, side3, side5)
         U_(Uside, side1, side6)
         R_(Rside, side3, side5)
         U(Uside, side1, side6)
         U(Uside, side1, side6)
         R(Rside, side3, side5)
         print("R' U' R U' R' U2 R")
      elif side6[1][0] == "y" and side2[0][1] == "y" and side3[0][1] == "y" and side4[0][1] == "y":
         R(Rside, side3, side5)
         U(Uside, side1, side6)
         R_(Rside, side3, side5)
         U(Uside, side1, side6)
         R(Rside, side3, side5)
         U(Uside, side1, side6)
         U(Uside, side1, side6)
         R_(Rside, side3, side5)
         print("R U R' U R U2 R'")
      elif side6[0][0] == "y" and side6[1][1] == "y" and side2[0][0] == "y" and side3[0][1] == "y":
         F(Fside, side2, side4)
         R_(Rside, side3, side5)
         F_(Fside, side2, side4)
         R(Rside, side3, side5)
         U(Uside, side1, side6)
         R(Rside, side3, side5)
         U_(Uside, side1, side6)
         R_(Rside, side3, side5)
         print("F R' F' R U R U' R'")
      elif side6[0][1] == "y" and side6[1][1] == "y" and side2[0][0] == "y" and side4[0][1] == "y":
         R(Rside, side3, side5)
         U(Uside, side1, side6)
         R_(Rside, side3, side5)
         U_(Uside, side1, side6)
         R_(Rside, side3, side5)
         F(Fside, side2, side4)
         R(Rside, side3, side5)
         F_(Fside, side2, side4)
         print("R U R' U' R' F R F'")
      elif side6[0][1] == "y" and side6[1][1] == "y" and side5[0][0] == "y" and side5[0][1] == "y":
         F(Fside, side2, side4)
         R(Rside, side3, side5)
         U(Uside, side1, side6)
         R_(Rside, side3, side5)
         U_(Uside, side1, side6)
         F_(Fside, side2, side4)
         print("F R U R' U' F'")
      elif side2[0][0] == "y" and side2[0][1] == "y" and side4[0][0] == "y" and side4[0][1] == "y":
         R(Rside, side3, side5)
         R(Rside, side3, side5)
         U(Uside, side1, side6)
         U(Uside, side1, side6)
         R_(Rside, side3, side5)
         U(Uside, side1, side6)
         U(Uside, side1, side6)
         R(Rside, side3, side5)
         R(Rside, side3, side5)
         print("R2 U2 R' U2 R2")
      elif side2[0][1] == "y" and side4[0][0] == "y" and side5[0][0] == "y" and side5[0][1] == "y":
         F(Fside, side2, side4)
         for i in range(2):
            R(Rside, side3, side5)
            U(Uside, side1, side6)
            R_(Rside, side3, side5)
            U_(Uside, side1, side6)
         F_(Fside, side2, side4)
         print("F ( R U R' U')*2 F'")
      if side6 == [["y", "y"],["y", "y"]]: break
      U(Uside, side1, side6)
      print("U")
def step3(side):
   side1 = side[0];side2 = side[1];side3 = side[2];side4 = side[3];side5 = side[4];side6 = side[5]
   reload()
   if side3[0][0] == side3[0][1]:
      U(Uside, side1, side6)
      U(Uside, side1, side6)
      print("U2")
   elif side4[0][0] == side4[0][1]:
      U_(Uside, side1, side6)
      print("U'")
   elif side2[0][0] == side2[0][1]:
      U(Uside, side1, side6)
      print("U")
   elif side3[0][0] != side3[0][1] and side2[0][0] != side2[0][1] and side4[0][0] != side4[0][1] and side5[0][0] != side5[0][1]:
      R(Rside, side3, side5)
      U(Uside, side1, side6)
      R_(Rside, side3, side5)
      F_(Fside, side2, side4)
      R(Rside, side3, side5)
      U(Uside, side1, side6)
      R_(Rside, side3, side5)
      U_(Uside, side1, side6)
      R_(Rside, side3, side5)
      F(Fside, side2, side4)
      R(Rside, side3, side5)
      R(Rside, side3, side5)
      U_(Uside, side1, side6)
      R_(Rside, side3, side5)
      print("R U R' F' R U R' U' R' F R2 U' R'")
   for i in range(4):
      if side5[0][0] == side5[0][1] and side2[0][0] == side2[0][1] and side3[0][0] == side3[0][1] and side4[0][0] == side4[0][1]: break
      if side5[0][0] == side5[0][1] and side2[0][0] != side2[0][1]:
         R(Rside, side3, side5)
         U(Uside, side1, side6)
         R_(Rside, side3, side5)
         F_(Fside, side2, side4)
         R(Rside, side3, side5)
         U(Uside, side1, side6)
         R_(Rside, side3, side5)
         U_(Uside, side1, side6)
         R_(Rside, side3, side5)
         F(Fside, side2, side4)
         R(Rside, side3, side5)
         R(Rside, side3, side5)
         U_(Uside, side1, side6)
         R_(Rside, side3, side5)
         print("R U R' F' R U R' U' R' F R2 U' R'")
      else:
         U(Uside, side1, side6)
         print("U")
def step4(side):
   side1 = side[0];side2 = side[1];side3 = side[2];side4 = side[3];side5 = side[4];side6 = side[5]
   reload()
   if side2[1][0] != side2[1][1] and side3[1][0] != side3[1][1] and side4[1][0] != side4[1][1] and side5[1][0] != side5[1][1]:
      R_(Rside, side3, side5)
      D_(Dside, side1, side6)
      R(Rside, side3, side5)
      F(Fside, side2, side4)
      R_(Rside, side3, side5)
      D_(Dside, side1, side6)
      R(Rside, side3, side5)
      D(Dside, side1, side6)
      R(Rside, side3, side5)
      F_(Fside, side2, side4)
      R(Rside, side3, side5)
      R(Rside, side3, side5)
      D(Dside, side1, side6)
      R(Rside, side3, side5)
      print("R' D' R F R' D' R D R F' R2 D R")
   for i in range(2):
      if side5[1][0] == side5[1][1] and side2[1][0] == side2[1][1] and side3[1][0] == side3[1][1] and side4[1][0] == side4[1][1]: break
      if side5[1][0] == side5[1][1]:
         R_(Rside, side3, side5)
         D_(Dside, side1, side6)
         R(Rside, side3, side5)
         F(Fside, side2, side4)
         R_(Rside, side3, side5)
         D_(Dside, side1, side6)
         R(Rside, side3, side5)
         D(Dside, side1, side6)
         R(Rside, side3, side5)
         F_(Fside, side2, side4)
         R(Rside, side3, side5)
         R(Rside, side3, side5)
         D(Dside, side1, side6)
         R(Rside, side3, side5)
         print("R' D' R F R' D' R D R F' R2 D R")
      elif side2[1][0] == side2[1][1]:
         D_(Dside, side1, side6)
         print("D'")
      elif side3[1][0] == side3[1][1]:
         D(Dside, side1, side6)
         D(Dside, side1, side6)
         print("D2")
      elif side4[1][0] == side4[1][1]:
         D(Dside, side1, side6)
         print("D")
   for i in range(4):
        if side5[1] != side5[0]:
            D(Dside, side1, side6)
            print("D")
print("公式如下:")
print("____________________")
step1(side)
step2(side)
step3(side)
step4(side)
print("____________________")
print("結果如下:")
print_cube(side)