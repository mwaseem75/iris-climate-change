Class dc.climatechange.utility
{

ClassMethod ImportDS() As %String
{
    //Dynamically create country table
    Do ..GetColTypes("/opt/irisapp/src/data/climatechange/FAOSTAT_data_11-24-2020.csv",.coltype)
    SET tableName= "dc.ClimateChange.Countries"
    SET qry = "CREATE TABLE "_tableName_" ("_coltype_")"
    SET rset = ##class(%SQL.Statement).%ExecDirect(,qry)
    //Check if table created successfully
    IF rset.%SQLCODE
    {
        WRITE rset.%Message,!          
    }
    ELSE
    {
    //Load DATA to country table 
        SET qry = "LOAD DATA FROM FILE  '/opt/irisapp/src/data/climatechange/FAOSTAT_data_11-24-2020.csv' INTO dc.ClimateChange.Countries USING {""from"":{""file"":{""header"":""0"",""skip"":""1""}}}"
        SET rset = ##class(%SQL.Statement).%ExecDirect(,qry)
        IF rset.%SQLCODE
        {
            WRITE rset.%Message,!  
        } 
    }

    //Dynamically create Climatechange data
    Do ..GetColTypes("/opt/irisapp/src/data/climatechange/Environment_Temperature_change_E_All_Data_NOFLAG.csv",.coltype)
    SET tableName= "dc.ClimateChange.Data"
    //SET coltype = "AreaCode NUMERIC(3,0), Area VARCHAR(100),MonthsCode NUMERIC(4,0),Months VARCHAR(20),ElementCode VARCHAR(4), Element VARCHAR(100), UNIT VARCHAR(3), Y1961 NUMERIC(7,3)"
    SET qry = "CREATE TABLE "_tableName_" ("_coltype_")"
    SET rset = ##class(%SQL.Statement).%ExecDirect(,qry)
    //Check if table created successfully
    IF rset.%SQLCODE
    {
         WRITE rset.%Message,!          
    }
    ELSE
    {
         //Load DATA statement
        SET qry = "LOAD DATA FROM FILE  '/opt/irisapp/src/data/climatechange/Environment_Temperature_change_E_All_Data_NOFLAG.csv' INTO dc.ClimateChange.Data USING {""from"":{""file"":{""header"":""0"",""skip"":""1""}}}"
        SET rset = ##class(%SQL.Statement).%ExecDirect(,qry)
        IF rset.%SQLCODE
        {
            
             WRITE rset.%Message,!  
        } 
    }
    return ""
}

// Get column lists based on the Header Row of CSV File

ClassMethod GetColTypes(filenamecsv As %String, ByRef coltype As %String, dlm As %String = ",")
{
    SET coltype=""
    SET stream=..GetStreamFromFile(filenamecsv)      
    SET header=stream.ReadLine() // Get Header columns
    //SET header=$ZCONVERT(header,"L")
    SET dataLine=stream.ReadLine() // Read First line of data
        
    //Read all the columns of header and add datatype against it        
    FOR i=1:1:($Length(header,dlm)) {
        kill types
        //Get datatype of the column
        DO ..GetDataType($Piece(dataLine,dlm,i),.types)
        SET type=..GetType(.types) 

        // if type is varchar then assign length 250
        IF type="VARCHAR" SET type="VARCHAR(250)"
        SET $Piece(coltype,dlm,i)=$TR($Piece(header,dlm,i)," ","")_" "_type
    }
    SET coltype=$TR(coltype,dlm,",")
    // change "." symbol in column names
    SET coltype=$TR(coltype,".","_")
}

ClassMethod GetStreamFromFile(filename As %String) As %Stream
{
    // create new stream and link to the file
    SET stream = ##Class(%Stream.FileCharacter).%New()
    SET stream.LineTerminator = $Char(13,10)
    $$$TOE(sc,stream.LinkToFile(filename))
    RETURN stream
}

ClassMethod GetDataType(value As %String, ByRef types) As %Status
{
  
   //Get datatype based on the first column value 
   if $IsvalidDouble(value) {
       if $I(types("DOUBLE"))
       if $L(value,".")>1,$L($P(value,".",2))<10 if $I(types("MONEY"))
       if ($L(value,".")=1) if $I(types("INTEGER"))
   quit $$$OK
   }
   if ..IsDate(value) {
       if $I(types("DATE")) 
       Quit $$$OK 
   }
   if $I(types("VARCHAR"))
   return $$$OK
}

ClassMethod GetType(ByRef types) As %String
{
    If $D(types("MONEY")),$D(types("DOUBLE")) {
        if types("MONEY")=types("DOUBLE") return "MONEY"
    }
    SET i=$Order(types(""))
    while i'="" { 
        SET typesI(types(i))=i
        SET i=$Order(types(i))
    }
    if $D(typesI) return typesI($Order(typesI(""),-1))
    return "VARCHAR"
}

ClassMethod IsDate(pVar As %String = "") As %Boolean
{
    SET sts=$$$YES
    Try {
        If $ZDateH(pVar,5)
    }
    Catch e {
        SET sts=$$$NO
    }
    Quit sts
}

}
