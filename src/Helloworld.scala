

object Helloworld {
  def addInt(a:Int,b:Int):Int = {
    var sum:Int =0
    var a:Int =3
    var b:Int =5
    sum = a+b
    return sum
  }
  
    def main(args:Array[String]) {
    println("hello world"+" "+addInt(1,3))
      
    }
  
}