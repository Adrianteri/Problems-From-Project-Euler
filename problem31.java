
import java.util.ArrayList;
import java.util.Iterator;


class Combinations
{
    private int oneP = 1;
    private int twoP = 2;
    private int fiveP = 5;
    private int tenP = 10;
    private int twentyP = 20;
    private int fiftyP = 50;
    private int oneEuro = 100;
    private int twoEuro = 200;

    private int count = 0;
    private ArrayList< Integer > myList = new ArrayList< Integer >();
    
    public ArrayList setArray()
    {
        myList.put( oneP );
        myList.put( twoP );
        myList.put( fiveP );
        myList.put( tenP );
        myList.put( twentyP );
        myList.put( fiftyP );
        myList.put( oneEuro );
        myList.put( twoEuro );

        return myList;
    }

    public int getCombinations()
    {
        //level 1
        //level 2
        //level 3
        //level 4
        //level 5
        //level 6
        //level 7
        

    return count; 

    }

    public void display()
    {
        System.out.Println( "The total no. of ways to produce E2 is " + count );

    }

    public static void main( String[] Args )
    {
        Combinations combs = new Combinations();
        combs.getCombinations();
        combs.display();

    }

}