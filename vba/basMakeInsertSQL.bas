Attribute VB_Name = "basMakeInsertSQL"
Option Explicit

' INSERT文生成ツール

' 設定項目に指定した行から情報を取得して、INSERT文を生成し、
' テキストファイルに保存します。
' テーブル名は、シート名から取得し、
' ファイル名は、テーブル名 + .sql で保存されます。
'
' データ型は、シングルクォーテーションが必要か判断する為だけなので、
' 正確なデータ型は必要ありません。（ v だけでもOK ）
'
'
'===== 設定項目 =================================================================
'■フィールド名を定義した行
Const ROW_FIELD_NAME As Integer = 2

'■データ型を定義した行（シングルクォーテーションが必要か判断するため）
Const ROW_DATA_TYPE As Integer = 3

'■データの開始行
Const ROW_DATA_START As Integer = 4
'================================================================================

'マクロ呼び出し元
Public Sub MakeInsertSQL()
    
    Dim strTableName As String
    Dim strFileName As String

    'ここを変更すれば、テーブル名と保存ファイル名を変更できます。

    'シート名をテーブル名に
    strTableName = ActiveSheet.Name
    
    'ファイル名もテーブル名を基に生成
    strFileName = ActiveWorkbook.Path & "\" & strTableName & ".sql"
    
    '実行
    Call MakeInsertSQL_Exec(strTableName, strFileName)
    
End Sub

'シートのデータからINSERT文を生成
'  引数： テーブル名, 保存ファイル名
Private Sub MakeInsertSQL_Exec(strTableName As String, strFileName As String)
Attribute MakeInsertSQL_Exec.VB_Description = ""
Attribute MakeInsertSQL_Exec.VB_ProcData.VB_Invoke_Func = " \n14"
    On Error GoTo ErrLabel
    
    Dim strInsert As String     'INSERT句
    Dim strValues As String     'VALUES句
    Dim strVal As String
    Dim strSql As String
    Dim intCnt As Integer
    Dim intCol As Integer
    Dim intRow As Integer
    Dim intColMax As Integer
    Dim intRowMax As Integer
    Dim strTypes() As String    'データ型格納配列
    
    
    'ファイルオープン
    Open strFileName For Output As #1
    
    'DELETE文（コメント）
    Print #1, "-- DELETE FROM " & strTableName & ";"
    
    'テーブル範囲全体を選択
    Selection.CurrentRegion.Select
    
    '行列範囲を取得
    intColMax = Selection.Columns.Count
    intRowMax = Selection.Rows.Count
    
    ReDim strTypes(intColMax) 'データ型格納配列
    
    'フィールド名を取得して、INSERT INTO 句を生成
    strInsert = "INSERT INTO " & strTableName & " ("
    For intCol = 1 To intColMax
        strInsert = strInsert & Cells(ROW_FIELD_NAME, intCol).Value & ","
    Next
    strInsert = Left(strInsert, Len(strInsert) - 1) '最後のカンマを除去
    strInsert = strInsert & ")"
    
    'データ型を取得
    For intCol = 1 To intColMax
        strTypes(intCol) = Cells(ROW_DATA_TYPE, intCol).Value
    Next
    
    'データを取得して VALUES 句を生成
    For intRow = ROW_DATA_START To intRowMax
        strValues = " VALUES ("
        For intCol = 1 To intColMax
            strVal = Cells(intRow, intCol).Value
            If strVal <> "" Then
                If NeedQuotes(strTypes(intCol)) Then
                    strValues = strValues & "'" & strVal & "'," '文字列, 日付
                Else
                    strValues = strValues & strVal & ","        '数値
                End If
            Else
                strValues = strValues & "NULL,"  '空白
            End If
        Next intCol
        strValues = Left(strValues, Len(strValues) - 1) '最後のカンマを除去
        strSql = strInsert & strValues & ");"
        Debug.Print strSql
        Print #1, strSql
        intCnt = intCnt + 1
    Next intRow
    
    MsgBox "件数： " & intCnt & "件" & vbCrLf & "保存先： " & strFileName, vbOKOnly, "出力完了"
    
ExitLabel:
    Close #1
    Exit Sub
ErrLabel:
    MsgBox Err.Description
    Resume ExitLabel
    
End Sub

'シングルクォーテーションで囲む必要があるか判断
Private Function NeedQuotes(ByVal strType As String) As Boolean

    If strType <> "" Then
        '文字列か日付型の場合
        If InStr(1, strType, "char", vbTextCompare) _
        Or InStr(1, strType, "text", vbTextCompare) _
        Or InStr(1, strType, "date", vbTextCompare) _
        Or InStr(1, strType, "time", vbTextCompare) _
        Or InStr(1, strType, "v", vbTextCompare) Then
            NeedQuotes = True
        End If
    End If
    
End Function
