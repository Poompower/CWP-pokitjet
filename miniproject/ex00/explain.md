# 📖 คำอธิบายโค้ด Mini Project (Rush00 - ex00) แบบละเอียดทุกบรรทัด

เอกสารนี้อธิบายการทำงานของโค้ดใน [miniproject/ex00/main.py](file:///d:/code/CWP-pokitjet/miniproject/ex00/main.py) และ [miniproject/ex00/checkmate.py](file:///d:/code/CWP-pokitjet/miniproject/ex00/checkmate.py) ทุกบรรทัด

---

## 📄 1. ไฟล์ `main.py`

```python
from checkmate import checkmate

def main():
    board = """\
R...
.K..
..P.
....\
"""
    checkmate(board)

if __name__ == "__main__":
    main()
```

### 🔍 อธิบายทีละบรรทัด:
- **บรรทัดที่ 1 (`from checkmate import checkmate`):** อิมพอร์ตฟังก์ชันชื่อ `checkmate` มาจากไฟล์ `checkmate.py` เพื่อนำมาเรียกใช้งาน
- **บรรทัดที่ 3 (`def main():`):** ประกาศฟังก์ชันหลัก `main()` ที่จะใช้ทดสอบส่งกระดานหมากรุกเข้าไปตรวจ
- **บรรทัดที่ 4 - 9 (`board = """\..."""`):** กำหนดตัวแปร `board` เก็บข้อความกระดานหมากรุกแบบหลายบรรทัด (ขนาด 4x4)
  - เครื่องหมาย `\` หลัง `"""` และ `....` ใส่ไว้เพื่อไม่ให้ติดช่องว่างขึ้นบรรทัดใหม่ที่หัวและท้าย
  - `R` (เรือ) อยู่ที่แถว 0 ช่อง 0
  - `K` (ขุน) อยู่ที่แถว 1 ช่อง 1
  - `P` (เบี้ย) อยู่ที่แถว 2 ช่อง 2
  - จุด `.` คือช่องว่าง
- **บรรทัดที่ 10 (`checkmate(board)`):** ส่งตัวแปร `board` เข้าไปให้ฟังก์ชัน `checkmate` คำนวณ
- **บรรทัดที่ 12 - 13 (`if __name__ == "__main__": main()`):** เช็คว่าถ้าไฟล์นี้ถูกรันโดยตรงจาก Terminal (`python main.py`) ให้เรียกฟังก์ชัน `main()` ทำงานทันที

---

## 📄 2. ไฟล์ `checkmate.py`

### 🔹 ส่วนที่ 1: ตรวจสอบความถูกต้องของ Input (Validation)

```python
def checkmate(board):
    if not isinstance(board, str) or not board:
        print("Error: board must be a valid non-empty string")
        return

    lines = board.splitlines()
    if lines and lines[0] == '':
        lines = lines[1:]
    if lines and lines[-1] == '':
        lines = lines[:-1]

    size = len(lines)
    if size == 0:
        print("Error: board cannot be empty")
        return

    # Check if the board is square
    for row in lines:
        if len(row) != size:
            print(f"Error: board must be square ({size}x{size}), but found a row with length {len(row)}")
            return
```

- **บรรทัดที่ 1 (`def checkmate(board):`):** ประกาศฟังก์ชัน `checkmate` รับพารามิเตอร์ `board` (ข้อความกระดานหมากรุก)
- **บรรทัดที่ 2 - 4 (`if not isinstance(board, str) or not board:`):** ตรวจสอบว่าถ้า `board` ไม่ใช่ข้อความ (String) หรือส่งค่าว่าง (`None`, `""`) มา ให้พิมพ์แจ้งเตือน `"Error: board must be a valid non-empty string"` แล้วหยุดทำงานทันที
- **บรรทัดที่ 6 - 10 (`lines = board.splitlines()...`):**
  - ตัดข้อความกระดานออกเป็นแถวๆ เก็บใน List `lines`
  - ลบบรรทัดว่างเปล่าที่อาจติดมาที่หัวหรือท้ายสุดของข้อความออกไป
- **บรรทัดที่ 12 - 15 (`size = len(lines)...`):** นับจำนวนแถวเก็บไว้ในตัวแปร `size` ถ้าไม่มีแถวเลย ให้พิมพ์แจ้งเตือน `"Error: board cannot be empty"` แล้วหยุดทำงาน
- **บรรทัดที่ 18 - 21 (`for row in lines: if len(row) != size: ...`):** วนลูปเช็คความยาวของทุกๆ แถวว่าเท่ากับ `size` หรือไม่ (กระดานต้องเป็นสี่เหลี่ยมจัตุรัส $N \times N$) ถ้ามีแถวไหนยาวไม่เท่ากัน ให้พิมพ์แจ้งเตือนพร้อมบอกขนาดที่ผิดพลาด เช่น `"Error: board must be square (4x4), but found a row with length 3"` แล้วหยุดทำงาน

---

### 🔹 ส่วนที่ 2: หาตำแหน่งของ King (K)

```python
    # Find King's position and verify there is exactly one King
    king_pos = None
    king_count = 0
    pieces = {'P', 'B', 'R', 'Q', 'K'}

    for r in range(size):
        for c in range(size):
            if lines[r][c] == 'K':
                king_pos = (r, c)
                king_count += 1

    if king_count == 0:
        print("Error: King ('K') not found on the board")
        return
    elif king_count > 1:
        print(f"Error: board must contain exactly one King ('K'), but found {king_count}")
        return

    kr, kc = king_pos
```

- **บรรทัดที่ 25 - 27:**
  - `king_pos`: ตัวแปรเก็บพิกัดแถวและคอลัมน์ของ King เริ่มต้นเป็น `None`
  - `king_count`: ตัวนับจำนวน King ในกระดาน
  - `pieces`: Set ของตัวหมากทั้งหมด เพื่อใช้เช็คว่าช่องไหนมีตัวหมากมาขวางทาง
- **บรรทัดที่ 29 - 33:** วนลูปดูทุกช่องในกระดาน (แถว `r`, คอลัมน์ `c`) ถ้าเจอตัวอักษร `'K'` ให้จำพิกัด `(r, c)` เก็บไว้ใน `king_pos` และบวกตัวนับ `king_count` เพิ่มขึ้น 1
- **บรรทัดที่ 35 - 40:** ตรวจสอบจำนวน King ในกระดาน:
  - ถ้าไม่มี King (`king_count == 0`) ➡️ พิมพ์ `"Error: King ('K') not found on the board"`
  - ถ้ามี King มากกว่า 1 ตัว (`king_count > 1`) ➡️ พิมพ์ `"Error: board must contain exactly one King ('K'), but found X"`
- **บรรทัดที่ 42 (`kr, kc = king_pos`):** แตกพิกัด King ออกมาเก็บเป็นตัวแปร `kr` (แถวของ King) และ `kc` (คอลัมน์ของ King)

---

### 🔹 ส่วนที่ 3: ตรวจสอบการโจมตีจาก Pawn (เบี้ย)

```python
    # 1. Check Pawn attack (Pawn attacks up-left and up-right)
    # So a pawn below the King at (kr + 1, kc - 1) or (kr + 1, kc + 1) attacks the King
    pawn_offsets = [(1, -1), (1, 1)]
    for dr, dc in pawn_offsets:
        r, c = kr + dr, kc + dc
        if 0 <= r < size and 0 <= c < size:
            if lines[r][c] == 'P':
                print("Success")
                return
```

- **บรรทัดที่ 38 (`pawn_offsets = [(1, -1), (1, 1)]`):** กำหนดพิกัดสัมพัทธ์ของเบี้ยที่สามารถกิน King ได้:
  - `(1, -1)` = ช่องล่างซ้ายของ King
  - `(1, 1)` = ช่องล่างขวาของ King  
  *(เพราะเบี้ยเดินพุ่งขึ้นบน ดังนั้นเบี้ยที่จะกิน King ได้ต้องอยู่ใต้ King 1 ช่องแล้วพุ่งเฉียงขึ้นมา)*
- **บรรทัดที่ 39 - 40:** วนลูปคำนวณพิกัดจริง `r` และ `c`
- **บรรทัดที่ 41:** เช็คว่าพิกัดนั้น **ไม่หลุดออกนอกขอบกระดาน**
- **บรรทัดที่ 42 - 44:** ถ้าช่องนั้นมีตัวอักษร `'P'` อยู่ แปลว่า **King โดนเบี้ยรุก!** ให้พิมพ์ `"Success"` แล้วจบการทำงานทันที

---

### 🔹 ส่วนที่ 4: ตรวจสอบการโจมตีแนวตรง (Rook และ Queen)

```python
    # 2. Check Orthogonal rays for Rook (R) or Queen (Q)
    orthogonal_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in orthogonal_dirs:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            piece = lines[r][c]
            if piece in ('R', 'Q'):
                print("Success")
                return
            elif piece in pieces:
                # Any other piece blocks the ray
                break
            r += dr
            c += dc
```

- **บรรทัดที่ 47:** กำหนด 4 ทิศทางแนวตรง: ขึ้น `(-1, 0)`, ลง `(1, 0)`, ซ้าย `(0, -1)`, ขวา `(0, 1)`
- **บรรทัดที่ 48 - 59:** ยิงลำแสง (Raycast) ออกไปทีละก้าวในแนวตรง 4 ทิศ:
  - บรรทัด 50: วนลูปก้าวออกไปเรื่อยๆ ตราบใดที่ยังไม่ตกขอบกระดาน
  - บรรทัด 51: ดึงค่าตัวอักษรในช่องนั้นมาดู
  - บรรทัด 52-54: ถ้าเจอตัว `'R'` (เรือ) หรือ `'Q'` (ควีน) เป็นตัวแรก ➡️ **King โดนรุก!** พิมพ์ `"Success"` แล้วจบการทำงานทันที
  - บรรทัด 55-57: ถ้าเจอตัวหมากอื่น (เช่น `'P'`, `'B'`) มาขวางทาง ➡️ ให้ `break` หยุดตรวจทิศนี้ทันที เพราะมันบังทางยิงอยู่
  - บรรทัด 58-59: ก้าวต่อไปยังช่องถัดไปในทิศทางเดิม

---

### 🔹 ส่วนที่ 5: ตรวจสอบการโจมตีแนวทแยง (Bishop และ Queen)

```python
    # 3. Check Diagonal rays for Bishop (B) or Queen (Q)
    diagonal_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in diagonal_dirs:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            piece = lines[r][c]
            if piece in ('B', 'Q'):
                print("Success")
                return
            elif piece in pieces:
                # Any other piece blocks the ray
                break
            r += dr
            c += dc
```

- **บรรทัดที่ 62:** กำหนด 4 ทิศทางแนวทแยง: ซ้ายบน `(-1, -1)`, ขวาบน `(-1, 1)`, ซ้ายล่าง `(1, -1)`, ขวาล่าง `(1, 1)`
- **บรรทัดที่ 63 - 74:** ยิงลำแสงแนวทแยงออกไปทั้ง 4 ทิศ:
  - บรรทัด 67-69: ถ้าเจอตัว `'B'` (บิชอป) หรือ `'Q'` (ควีน) เป็นตัวแรก ➡️ **King โดนรุก!** พิมพ์ `"Success"` แล้วจบการทำงานทันที
  - บรรทัด 70-72: ถ้าเจอตัวหมากอื่นมาขวางทาง ให้ `break` หยุดสแกนทิศนี้

---

### 🔹 ส่วนที่ 6: สรุปผลถ้า King ปลอดภัย

```python
    print("Fail")
```

- **บรรทัดที่ 76:** ถ้าสแกนครบหมดทุกทิศแล้ว ไม่มีหมากตัวไหนกิน King ได้เลย แปลว่า **King ปลอดภัย** ให้พิมพ์คำว่า `"Fail"` ออกมาตามที่โจทย์กำหนด
