<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis labelsEnabled="0" simplifyMaxScale="1" simplifyDrawingHints="0" simplifyLocal="1" version="3.7.0-Master" simplifyAlgorithm="0" styleCategories="AllStyleCategories" minScale="1e+8" readOnly="0" hasScaleBasedVisibilityFlag="0" simplifyDrawingTol="1" maxScale="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 type="singleSymbol" symbollevels="0" enableorderby="0" forceraster="0">
    <symbols>
      <symbol type="marker" clip_to_extent="1" alpha="1" name="0" force_rhr="0">
        <layer pass="0" enabled="1" class="SimpleMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="125,139,143,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <customproperties/>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks type="StringList">
      <Option type="QString" value=""/>
    </activeChecks>
    <checkConfiguration/>
  </geometryOptions>
  <fieldConfiguration>
    <field name="id">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="nomeabrev">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="geometriaaproximada">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="Map" name="map">
              <Option type="QString" value="2" name="Não"/>
              <Option type="QString" value="1" name="Sim"/>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="tiporef">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="Map" name="map">
              <Option type="QString" value="1" name="Altimétrico"/>
              <Option type="QString" value="3" name="Planialtimétrico"/>
              <Option type="QString" value="2" name="Planimétrico"/>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="latitude">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="longitude">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="altitudeortometrica">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sistemageodesico">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="Map" name="map">
              <Option type="QString" value="5" name="Astro Chuá"/>
              <Option type="QString" value="4" name="Córrego Alegre"/>
              <Option type="QString" value="6" name="Outra referência"/>
              <Option type="QString" value="1" name="SAD-69"/>
              <Option type="QString" value="2" name="SIRGAS"/>
              <Option type="QString" value="3" name="WGS-84"/>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="referencialaltim">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="Map" name="map">
              <Option type="QString" value="2" name="Imbituba"/>
              <Option type="QString" value="4" name="Local"/>
              <Option type="QString" value="5" name="Outra referência"/>
              <Option type="QString" value="3" name="Santana"/>
              <Option type="QString" value="1" name="Torres"/>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="outrarefalt">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="outrarefplan">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="orgaoenteresp">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="codponto">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="obs">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="tipoptocontrole">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="Map" name="map">
              <Option type="QString" value="99" name="Outros"/>
              <Option type="QString" value="13" name="Ponto Fotogramétrico"/>
              <Option type="QString" value="12" name="Ponto Perspectivo"/>
              <Option type="QString" value="9" name="Ponto de Controle"/>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="materializado">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="Map" name="map">
              <Option type="QString" value="0" name="Desconhecido"/>
              <Option type="QString" value="2" name="Não"/>
              <Option type="QString" value="1" name="Sim"/>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="codprojeto">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias field="id" name="" index="0"/>
    <alias field="nomeabrev" name="" index="1"/>
    <alias field="geometriaaproximada" name="" index="2"/>
    <alias field="tiporef" name="" index="3"/>
    <alias field="latitude" name="" index="4"/>
    <alias field="longitude" name="" index="5"/>
    <alias field="altitudeortometrica" name="" index="6"/>
    <alias field="sistemageodesico" name="" index="7"/>
    <alias field="referencialaltim" name="" index="8"/>
    <alias field="outrarefalt" name="" index="9"/>
    <alias field="outrarefplan" name="" index="10"/>
    <alias field="orgaoenteresp" name="" index="11"/>
    <alias field="codponto" name="" index="12"/>
    <alias field="obs" name="" index="13"/>
    <alias field="tipoptocontrole" name="" index="14"/>
    <alias field="materializado" name="" index="15"/>
    <alias field="codprojeto" name="" index="16"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="id" expression="" applyOnUpdate="0"/>
    <default field="nomeabrev" expression="" applyOnUpdate="0"/>
    <default field="geometriaaproximada" expression="" applyOnUpdate="0"/>
    <default field="tiporef" expression="" applyOnUpdate="0"/>
    <default field="latitude" expression="" applyOnUpdate="0"/>
    <default field="longitude" expression="" applyOnUpdate="0"/>
    <default field="altitudeortometrica" expression="" applyOnUpdate="0"/>
    <default field="sistemageodesico" expression="" applyOnUpdate="0"/>
    <default field="referencialaltim" expression="" applyOnUpdate="0"/>
    <default field="outrarefalt" expression="" applyOnUpdate="0"/>
    <default field="outrarefplan" expression="" applyOnUpdate="0"/>
    <default field="orgaoenteresp" expression="" applyOnUpdate="0"/>
    <default field="codponto" expression="" applyOnUpdate="0"/>
    <default field="obs" expression="" applyOnUpdate="0"/>
    <default field="tipoptocontrole" expression="" applyOnUpdate="0"/>
    <default field="materializado" expression="" applyOnUpdate="0"/>
    <default field="codprojeto" expression="" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint field="id" unique_strength="1" exp_strength="0" constraints="3" notnull_strength="1"/>
    <constraint field="nomeabrev" unique_strength="0" exp_strength="0" constraints="0" notnull_strength="0"/>
    <constraint field="geometriaaproximada" unique_strength="0" exp_strength="0" constraints="1" notnull_strength="1"/>
    <constraint field="tiporef" unique_strength="0" exp_strength="0" constraints="1" notnull_strength="1"/>
    <constraint field="latitude" unique_strength="0" exp_strength="0" constraints="0" notnull_strength="0"/>
    <constraint field="longitude" unique_strength="0" exp_strength="0" constraints="0" notnull_strength="0"/>
    <constraint field="altitudeortometrica" unique_strength="0" exp_strength="0" constraints="0" notnull_strength="0"/>
    <constraint field="sistemageodesico" unique_strength="0" exp_strength="0" constraints="1" notnull_strength="1"/>
    <constraint field="referencialaltim" unique_strength="0" exp_strength="0" constraints="1" notnull_strength="1"/>
    <constraint field="outrarefalt" unique_strength="0" exp_strength="0" constraints="0" notnull_strength="0"/>
    <constraint field="outrarefplan" unique_strength="0" exp_strength="0" constraints="0" notnull_strength="0"/>
    <constraint field="orgaoenteresp" unique_strength="0" exp_strength="0" constraints="0" notnull_strength="0"/>
    <constraint field="codponto" unique_strength="0" exp_strength="0" constraints="0" notnull_strength="0"/>
    <constraint field="obs" unique_strength="0" exp_strength="0" constraints="0" notnull_strength="0"/>
    <constraint field="tipoptocontrole" unique_strength="0" exp_strength="0" constraints="1" notnull_strength="1"/>
    <constraint field="materializado" unique_strength="0" exp_strength="0" constraints="1" notnull_strength="1"/>
    <constraint field="codprojeto" unique_strength="0" exp_strength="0" constraints="0" notnull_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="id" desc="" exp=""/>
    <constraint field="nomeabrev" desc="" exp=""/>
    <constraint field="geometriaaproximada" desc="" exp=""/>
    <constraint field="tiporef" desc="" exp=""/>
    <constraint field="latitude" desc="" exp=""/>
    <constraint field="longitude" desc="" exp=""/>
    <constraint field="altitudeortometrica" desc="" exp=""/>
    <constraint field="sistemageodesico" desc="" exp=""/>
    <constraint field="referencialaltim" desc="" exp=""/>
    <constraint field="outrarefalt" desc="" exp=""/>
    <constraint field="outrarefplan" desc="" exp=""/>
    <constraint field="orgaoenteresp" desc="" exp=""/>
    <constraint field="codponto" desc="" exp=""/>
    <constraint field="obs" desc="" exp=""/>
    <constraint field="tipoptocontrole" desc="" exp=""/>
    <constraint field="materializado" desc="" exp=""/>
    <constraint field="codprojeto" desc="" exp=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions/>
  <attributetableconfig sortExpression="" sortOrder="0" actionWidgetStyle="dropDown">
    <columns/>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable/>
  <labelOnTop/>
  <widgets/>
  <previewExpression></previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>
