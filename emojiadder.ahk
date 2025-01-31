PasteFromFile() {
    scriptDir := A_ScriptDir
    outputFilePath := scriptDir . "\output.txt"
    
    IfExist, %outputFilePath%
    {
        FileEncoding, UTF-8
        FileRead, OutputVar, %outputFilePath%
        OutputVar := RegExReplace(OutputVar, "\r?\n$", "") 
        if (OutputVar = "")
        {
            MsgBox, Error: output.txt is empty or not written correctly.
            return "" ;
        }
        return OutputVar
    }
    else
    {
        MsgBox, output.txt does not exist in the script directory.
    }
}

Numpad4::
NumpadLeft::
{
 Menu, MyMenu, Add, 1 Emoji Appender, item1
 Menu, MyMenu, Add, 2 Response Generator, item2
 Menu, MyMenu, Show 
}
Return

item1:
    ClipSaved := ClipboardAll  
    Clipboard := ""  
    Send, ^c  
    ClipWait, 1  

    if (Clipboard != "")  
    {
        Clipboard := RegExReplace(Clipboard, "\r?\n+", " ")
        RunWait, %ComSpec% /c pythonw "%A_ScriptDir%\emoji_wrapper.py" "%Clipboard%" > "%A_ScriptDir%\output.txt", , Hide
        Sleep, 500  
        output := PasteFromFile()
        if (output != "")
        {
            Send, {Right}
            SendInput, %output%
        }
    }
    else
    {
        MsgBox, No text selected!
    }

    Clipboard := ClipSaved  
    return

item2:
    ClipSaved := ClipboardAll  
    Clipboard := ""  
    Send, ^c  
    ClipWait, 1  

    if (Clipboard != "")  
    {
        Clipboard := RegExReplace(Clipboard, "\r?\n+", " ")
        RunWait, %ComSpec% /c pythonw "%A_ScriptDir%\reply_wrapper.py" "%Clipboard%" > "%A_ScriptDir%\output.txt", , Hide
        Sleep, 500  
        output := PasteFromFile()
    }
    else
    {
        MsgBox, No text selected!
    }

    Clipboard := ClipSaved  
    if (output != "")
    {
        Clipboard := output
    }
    return