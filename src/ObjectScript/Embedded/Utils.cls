Class Embedded.Utils
{

ClassMethod GetNameSpace() As %Status
{

    Return $namespace
}

ClassMethod SetNameSpace(pNameSpace) As %Status
{
    zn pNameSpace
    Return $namespace
}

ClassMethod SetGbl() As %Status
{
    Set start = $ZH // get current time
    Kill ^Test.Global
    For i = 1:1:10000 {
    Set ^Test.Global(i) = i
    }
    Set elap = $ZH - start // get
    Return $namespace
}

}
