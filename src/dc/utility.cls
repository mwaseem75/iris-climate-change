Class dc.utility
{

ClassMethod ImportDS() As %String
{
    //Create table query
    SET qry = "CREATE TABLE Sample.Person1(CountryCode INT,Country VARCHAR(50),M49Code VARCHAR(3),ISO2Code VARCHAR(2),ISO3Code VARCHAR(3),StartYear INT,EndYear INT)"
    //Execute Query
    SET rset = ##class(%SQL.Statement).%ExecDirect(,qry)
    //Check if table created successfully
    IF rset.%SQLCODE
    {
        WRITE rset.%Message,!          
    }
    ELSE
    {
    //Load DATA statement
        SET qry = "LOAD DATA FROM FILE  '/irisdev/app/src/data/climatechange/FAOSTAT_data_11-24-2020.csv' INTO Sample.Person1 USING {""from"":{""file"":{""header"":""0""}}}"
        SET rset = ##class(%SQL.Statement).%ExecDirect(,qry)
        IF rset.%SQLCODE
        {
             WRITE rset.%Message,!  
        } 
    }
         
    return ""
}

}
