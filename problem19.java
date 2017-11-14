import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Calendars
{
    private int leepYearsDiv = 4;
    private int leepYearCenturyDiv = 400;
    private List< Integer > nonLeepYear = Arrays.asList( 31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31 );
    private List< Integer > leepYear = Arrays.asList( 31, 29, 31, 30, 31, 30, 31, 30, 31, 30, 31 );
    private int specialMonths = 1; 
    private int startYear = 1901;
    private int endYear = 2000;
    private int period = 0;
    private int week = 7;
    private ArrayList< Integer > sundaysOnFirstOfTheMonth = new ArrayList< Integer >();
    private ArrayList< Integer > leepYears = new ArrayList< Integer >();


    public int getTimePeriod()
    {
        return period = endYear - startYear;

    }

    public ArrayList< Integer > getLeepYears()
    {
        for(int start=startYear; start<= endYear; start++)
        {
            if(start % leepYearsDiv == 0 || start % leepYearCenturyDiv == 0)
                leepYears.put(start);
                
        }

        return leepYears;
    }

    public int countSundays()
    {
        //first sunday from 1901 Jan is 6th
        int firstSunday = 6;
        for(int years = 0; years < period; years++ )
        {
            if(years !)
        }
    }

    public static void main(String [] args)
    {

    }



}