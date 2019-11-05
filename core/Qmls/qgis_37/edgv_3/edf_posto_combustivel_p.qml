<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'><qgis version="2.6.0-Brighton" minimumScale="1" maximumScale="1" simplifyDrawingHints="0" minLabelScale="0" maxLabelScale="1e+08" simplifyDrawingTol="1" simplifyMaxScale="1" hasScaleBasedVisibilityFlag="0" simplifyLocal="1" scaleBasedLabelVisibilityFlag="0"><edittypes><edittype widgetv2type="ValueMap" name="administracao"><widgetv2config fieldEditable="1" labelOnTop="0"><value key="Estadual/Distrital" value="3"/><value key="Federal" value="2"/><value key="Concessionada" value="5"/><value key="Municipal" value="4"/><value key="Privada" value="6"/><value key="Desconhecida" value="95"/><value key="Não aplicável" value="97"/></widgetv2config></edittype><edittype widgetv2type="ValueRelation" name="classeativecon"><widgetv2config OrderByValue="0" AllowNull="1" FilterExpression="code in (10,11,12,13,14,15,16,17,18,19,2,20,21,22,23,24,25,26,27,28,29,3,30,31,32,33,34,35,36,4,5,6,7,8,9,95,98,99)" UseCompleter="0" fieldEditable="1" Key="code" Layer="classe_ativ_econ" Value="code_name" labelOnTop="0" AllowMulti="1"/></edittype><edittype widgetv2type="ValueMap" name="cultura"><widgetv2config fieldEditable="1" labelOnTop="0"><value key="Sim" value="1"/><value key="Não" value="0"/><value key="Desconhecido" value="95"/></widgetv2config></edittype><edittype widgetv2type="ValueRelation" name="divisaoativecon"><widgetv2config OrderByValue="0" AllowNull="1" FilterExpression="code in (1,10,11,13,14,15,16,17,18,19,2,20,21,22,23,24,25,27,28,29,30,31,32,33,34,35,36,37,45,5,50,51,52,55,74,92,95,99)" UseCompleter="0" fieldEditable="1" Key="code" Layer="divisao_ativ_econ" Value="code_name" labelOnTop="0" AllowMulti="1"/></edittype><edittype widgetv2type="ValueRelation" name="finalidade"><widgetv2config OrderByValue="0" AllowNull="1" FilterExpression="code in (1,2,3,4,95,99)" UseCompleter="0" fieldEditable="1" Key="code" Layer="finalidade_cultura" Value="code_name" labelOnTop="0" AllowMulti="1"/></edittype><edittype widgetv2type="ValueMap" name="geometriaaproximada"><widgetv2config fieldEditable="1" labelOnTop="0"><value key="Sim" value="1"/><value key="Não" value="0"/></widgetv2config></edittype><edittype widgetv2type="ValueRelation" name="grupoativecon"><widgetv2config OrderByValue="0" AllowNull="1" FilterExpression="code in (15,16,19,20,23,30,31,32,6,8,95,98,99)" UseCompleter="0" fieldEditable="1" Key="code" Layer="grupo_ativ_econ" Value="code_name" labelOnTop="0" AllowMulti="1"/></edittype><edittype widgetv2type="TextEdit" name="id"><widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/></edittype><edittype widgetv2type="TextEdit" name="id_assentamento_precario"><widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/></edittype><edittype widgetv2type="TextEdit" name="id_complexo_habitacional"><widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/></edittype><edittype widgetv2type="TextEdit" name="id_condominio"><widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/></edittype><edittype widgetv2type="TextEdit" name="id_conjunto_habitacional"><widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/></edittype><edittype widgetv2type="TextEdit" name="id_estacao_ferroviaria"><widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/></edittype><edittype widgetv2type="TextEdit" name="id_estacao_metroviaria"><widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/></edittype><edittype widgetv2type="TextEdit" name="id_estacao_rodoviaria"><widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/></edittype><edittype widgetv2type="TextEdit" name="id_estrut_apoio"><widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/></edittype><edittype widgetv2type="TextEdit" name="id_estrut_transporte"><widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/></edittype><edittype widgetv2type="TextEdit" name="id_terminal_ferroviario"><widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/></edittype><edittype widgetv2type="TextEdit" name="id_terminal_hidroviario"><widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/></edittype><edittype widgetv2type="TextEdit" name="id_terminal_rodoviario"><widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/></edittype><edittype widgetv2type="ValueMap" name="matconstr"><widgetv2config fieldEditable="1" labelOnTop="0"><value key="Outros" value="99"/><value key="Terra" value="23"/><value key="Alvenaria" value="1"/><value key="Metal" value="3"/><value key="Concreto" value="2"/><value key="Madeira" value="5"/><value key="Rocha" value="4"/><value key="Fibra" value="8"/><value key="Desconhecido" value="95"/><value key="Não aplicável" value="97"/></widgetv2config></edittype><edittype widgetv2type="ValueMap" name="operacional"><widgetv2config fieldEditable="1" labelOnTop="0"><value key="Sim" value="1"/><value key="Não" value="0"/><value key="Desconhecido" value="95"/></widgetv2config></edittype><edittype widgetv2type="ValueMap" name="proprioadm"><widgetv2config fieldEditable="1" labelOnTop="0"><value key="Sim" value="1"/><value key="Não" value="0"/></widgetv2config></edittype><edittype widgetv2type="ValueMap" name="situacaofisica"><widgetv2config fieldEditable="1" labelOnTop="0"><value key="Abandonada" value="1"/><value key="Em construção" value="3"/><value key="Destruída" value="2"/><value key="Construída" value="5"/><value key="Planejada" value="4"/><value key="Construída" value="7"/><value key="Construída, mas em obras" value="6"/><value key="Desconhecida" value="95"/><value key="Não aplicável" value="97"/></widgetv2config></edittype><edittype widgetv2type="ValueRelation" name="tipoedifcomercserv"><widgetv2config OrderByValue="0" AllowNull="1" FilterExpression="code in (19)" UseCompleter="0" fieldEditable="1" Key="code" Layer="tipo_edif_comerc_serv" Value="code_name" labelOnTop="0" AllowMulti="1"/></edittype><edittype widgetv2type="ValueMap" name="turistica"><widgetv2config fieldEditable="1" labelOnTop="0"><value key="Sim" value="1"/><value key="Não" value="0"/><value key="Desconhecido" value="95"/></widgetv2config></edittype></edittypes></qgis>
