Attribute VB_Name = "basMakeInsertSQL"
Option Explicit

' INSERT�������c�[��

' �ݒ荀�ڂɎw�肵���s��������擾���āAINSERT���𐶐����A
' �e�L�X�g�t�@�C���ɕۑ����܂��B
' �e�[�u�����́A�V�[�g������擾���A
' �t�@�C�����́A�e�[�u���� + .sql �ŕۑ�����܂��B
'
' �f�[�^�^�́A�V���O���N�H�[�e�[�V�������K�v�����f����ׂ����Ȃ̂ŁA
' ���m�ȃf�[�^�^�͕K�v����܂���B�i v �����ł�OK �j
'
'
'===== �ݒ荀�� =================================================================
'���t�B�[���h�����`�����s
Const ROW_FIELD_NAME As Integer = 2

'���f�[�^�^���`�����s�i�V���O���N�H�[�e�[�V�������K�v�����f���邽�߁j
Const ROW_DATA_TYPE As Integer = 3

'���f�[�^�̊J�n�s
Const ROW_DATA_START As Integer = 4
'================================================================================

'�}�N���Ăяo����
Public Sub MakeInsertSQL()
    
    Dim strTableName As String
    Dim strFileName As String

    '������ύX����΁A�e�[�u�����ƕۑ��t�@�C������ύX�ł��܂��B

    '�V�[�g�����e�[�u������
    strTableName = ActiveSheet.Name
    
    '�t�@�C�������e�[�u��������ɐ���
    strFileName = ActiveWorkbook.Path & "\" & strTableName & ".sql"
    
    '���s
    Call MakeInsertSQL_Exec(strTableName, strFileName)
    
End Sub

'�V�[�g�̃f�[�^����INSERT���𐶐�
'  �����F �e�[�u����, �ۑ��t�@�C����
Private Sub MakeInsertSQL_Exec(strTableName As String, strFileName As String)
Attribute MakeInsertSQL_Exec.VB_Description = ""
Attribute MakeInsertSQL_Exec.VB_ProcData.VB_Invoke_Func = " \n14"
    On Error GoTo ErrLabel
    
    Dim strInsert As String     'INSERT��
    Dim strValues As String     'VALUES��
    Dim strVal As String
    Dim strSql As String
    Dim intCnt As Integer
    Dim intCol As Integer
    Dim intRow As Integer
    Dim intColMax As Integer
    Dim intRowMax As Integer
    Dim strTypes() As String    '�f�[�^�^�i�[�z��
    
    
    '�t�@�C���I�[�v��
    Open strFileName For Output As #1
    
    'DELETE���i�R�����g�j
    Print #1, "-- DELETE FROM " & strTableName & ";"
    
    '�e�[�u���͈͑S�̂�I��
    Selection.CurrentRegion.Select
    
    '�s��͈͂��擾
    intColMax = Selection.Columns.Count
    intRowMax = Selection.Rows.Count
    
    ReDim strTypes(intColMax) '�f�[�^�^�i�[�z��
    
    '�t�B�[���h�����擾���āAINSERT INTO ��𐶐�
    strInsert = "INSERT INTO " & strTableName & " ("
    For intCol = 1 To intColMax
        strInsert = strInsert & Cells(ROW_FIELD_NAME, intCol).Value & ","
    Next
    strInsert = Left(strInsert, Len(strInsert) - 1) '�Ō�̃J���}������
    strInsert = strInsert & ")"
    
    '�f�[�^�^���擾
    For intCol = 1 To intColMax
        strTypes(intCol) = Cells(ROW_DATA_TYPE, intCol).Value
    Next
    
    '�f�[�^���擾���� VALUES ��𐶐�
    For intRow = ROW_DATA_START To intRowMax
        strValues = " VALUES ("
        For intCol = 1 To intColMax
            strVal = Cells(intRow, intCol).Value
            If strVal <> "" Then
                If NeedQuotes(strTypes(intCol)) Then
                    strValues = strValues & "'" & strVal & "'," '������, ���t
                Else
                    strValues = strValues & strVal & ","        '���l
                End If
            Else
                strValues = strValues & "NULL,"  '��
            End If
        Next intCol
        strValues = Left(strValues, Len(strValues) - 1) '�Ō�̃J���}������
        strSql = strInsert & strValues & ");"
        Debug.Print strSql
        Print #1, strSql
        intCnt = intCnt + 1
    Next intRow
    
    MsgBox "�����F " & intCnt & "��" & vbCrLf & "�ۑ���F " & strFileName, vbOKOnly, "�o�͊���"
    
ExitLabel:
    Close #1
    Exit Sub
ErrLabel:
    MsgBox Err.Description
    Resume ExitLabel
    
End Sub

'�V���O���N�H�[�e�[�V�����ň͂ޕK�v�����邩���f
Private Function NeedQuotes(ByVal strType As String) As Boolean

    If strType <> "" Then
        '�����񂩓��t�^�̏ꍇ
        If InStr(1, strType, "char", vbTextCompare) _
        Or InStr(1, strType, "text", vbTextCompare) _
        Or InStr(1, strType, "date", vbTextCompare) _
        Or InStr(1, strType, "time", vbTextCompare) _
        Or InStr(1, strType, "v", vbTextCompare) Then
            NeedQuotes = True
        End If
    End If
    
End Function
