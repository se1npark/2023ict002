x, y, w, h = map(int, input().split()) 

minVert = min(x, w - x) 
minHori = min(y, h - y) 

minDIs = min(minVert, minHori) 

print(minDIs) 