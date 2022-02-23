public class numPyramid{

    public void drawPyramid(){
        int length = 5;
        
        for (int i=1; i<=5;i++)
        {
            for (int space = length-i; space>0; space--)
            {
                System.out.print(" ");
            }
            for (int x=1; x<=i; x++)
            {
                System.out.print(x);
            }
            for (int y=i-1; y>0; y--)
            {
                System.out.print(y);
            }
            System.out.print("\n");
        }
    }
}
        
