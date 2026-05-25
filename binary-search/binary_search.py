def binary_search(list, item):
  down = 0;
  high = len(list) - 1;

  while down <= high:
    middle = (down + high) // 2;
    shot = list[middle];
    if shot == item:
      return middle;
    if shot > item:
      high = middle - 1;
    else:
      down = middle + 1;
  return None;


students_ages = [11,12,13,14,15,16,17,18];

print(binary_search(students_ages, 13));