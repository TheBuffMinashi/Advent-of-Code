count = 0
for item in os.listdir(input_t):

  # Read the image from the path
  path   = os.path.join(input_t , item)
  image  = cv2.imread(path, -1)
  (hei,wid,_) = image.shape 

  # Grayscale and blur the image
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  blur = cv2.GaussianBlur(gray, (3,3), 0)
  
  # Threshold the image
  thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

  # Retrieve contours 
  contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

  # Create box-list
  box = []

  # Get position (x,y), width and height for every contour 
  for c in contours:
      x, y, w, h = cv2.boundingRect(c)
      box.append([x,y,w,h])

  # Create separate lists for all values
  heights=[]
  widths=[]
  xs=[]
  ys=[]

  # Store values in lists
  for b in box:
      heights.append(b[3])
      widths.append(b[2])
      xs.append(b[0])
      ys.append(b[1])

  # Retrieve minimum and maximum of lists
  min_height = np.min(heights)
  min_width = np.min(widths)
  min_x = np.min(xs)
  min_y = np.min(ys)
  max_y = np.max(ys)
  max_x = np.max(xs)

  # Retrieve height where y is maximum (edge at bottom, last row of table)
  for b in box:
      if b[1] == max_y:
          max_y_height = b[3]

  # Retrieve width where x is maximum (rightmost edge, last column of table)
  for b in box:
      if b[0] == max_x:
          max_x_width = b[2]

  # Obtain horizontal lines mask
  horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (50,1))
  horizontal_mask = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=1)
  horizontal_mask = cv2.dilate(horizontal_mask, horizontal_kernel, iterations=1)

  # Obtain vertical lines mask
  vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,50))
  vertical_mask = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, vertical_kernel, iterations=1)
  vertical_mask= cv2.dilate(vertical_mask, vertical_kernel, iterations=1)

  # Bitwise-and masks together
  result = 255 - cv2.bitwise_or(vertical_mask, horizontal_mask)

  # Cropping the image to the table size
  crop_img = result[(min_y+5):(max_y+max_y_height), (min_x):(max_x+max_x_width+5)]

  # Creating a new image and filling it with white background
  img_white = np.zeros((hei, wid), np.uint8)
  img_white[:, 0:wid] = (255)

  # Retrieve the coordinates of the center of the image
  x_offset = int((wid - crop_img.shape[1])/2)
  y_offset = int((hei - crop_img.shape[0])/2)

  # Placing the cropped and repaired table into the white background
  img_white[ y_offset:y_offset+crop_img.shape[0], x_offset:x_offset+crop_img.shape[1]] = crop_img
  Final = gray + (~img_white) 
  cv2.imwrite(os.path.join(output_p, item), Final)
