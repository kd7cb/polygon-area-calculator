class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_height(self, newheight):
    self.height = newheight

  def set_width(self, newwidth):
    self.width = newwidth

  def get_area(self):
    self.area = self.width*self.height
    return self.area

  def get_perimeter(self):
    self.perimeter = (2*self.width)+(2*self.height)
    return self.perimeter

  def get_diagonal(self):
    self.diagonal = ((self.width**2) + (self.height**2))**0.5
    return self.diagonal

  def get_picture(self):
    printstr = ""
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      for x in range(self.height):
        printstr = printstr + "*"*self.width + '\n'
    return str(printstr)

  def __str__(self):
    repstr = "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
    return repstr

  def get_amount_inside(self, Rectangle):
    fwidth = Rectangle.width
    fheight = Rectangle.height

    fitx = self.width / fwidth
    fitx = fitx - (fitx%1)
    fity = self.height / fheight 
    fity = fity - (fity%1)
    
    totalfit = fitx*fity

    return int(totalfit)
  
class Square(Rectangle):

  def __init__(self,side):
    self.height = side
    self.width = side

  def set_side(self,newside):
    self.height = newside
    self.width = newside

  def __str__(self):
    repstr = "Square(side=" + str(self.width) + ")"
    return repstr