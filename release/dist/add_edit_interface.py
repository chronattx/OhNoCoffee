a = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>300</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QLineEdit" name="descriptionEdit">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>130</y>
     <width>113</width>
     <height>20</height>
    </rect>
   </property>
  </widget>
  <widget class="QLineEdit" name="kindEdit">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>40</y>
     <width>113</width>
     <height>20</height>
    </rect>
   </property>
  </widget>
  <widget class="QLineEdit" name="gradeEdit">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>70</y>
     <width>113</width>
     <height>20</height>
    </rect>
   </property>
  </widget>
  <widget class="QRadioButton" name="addBtn">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>10</y>
     <width>201</width>
     <height>17</height>
    </rect>
   </property>
   <property name="text">
    <string>Добавить</string>
   </property>
  </widget>
  <widget class="QRadioButton" name="changeBtn">
   <property name="geometry">
    <rect>
     <x>270</x>
     <y>10</y>
     <width>121</width>
     <height>20</height>
    </rect>
   </property>
   <property name="text">
    <string>Изменить</string>
   </property>
  </widget>
  <widget class="QSpinBox" name="idEdit">
   <property name="geometry">
    <rect>
     <x>270</x>
     <y>40</y>
     <width>42</width>
     <height>22</height>
    </rect>
   </property>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>130</x>
     <y>40</y>
     <width>81</width>
     <height>16</height>
    </rect>
   </property>
   <property name="text">
    <string>сорт</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_2">
   <property name="geometry">
    <rect>
     <x>130</x>
     <y>70</y>
     <width>201</width>
     <height>21</height>
    </rect>
   </property>
   <property name="text">
    <string>степень обжарки</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_3">
   <property name="geometry">
    <rect>
     <x>320</x>
     <y>50</y>
     <width>43</width>
     <height>13</height>
    </rect>
   </property>
   <property name="text">
    <string>id</string>
   </property>
  </widget>
  <widget class="QRadioButton" name="grindBtn">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>100</y>
     <width>131</width>
     <height>21</height>
    </rect>
   </property>
   <property name="text">
    <string>молотый</string>
   </property>
  </widget>
  <widget class="QRadioButton" name="beanBtn">
   <property name="geometry">
    <rect>
     <x>160</x>
     <y>100</y>
     <width>191</width>
     <height>21</height>
    </rect>
   </property>
   <property name="text">
    <string>в зёрнах</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_4">
   <property name="geometry">
    <rect>
     <x>130</x>
     <y>131</y>
     <width>161</width>
     <height>20</height>
    </rect>
   </property>
   <property name="text">
    <string>описание</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_5">
   <property name="geometry">
    <rect>
     <x>130</x>
     <y>160</y>
     <width>43</width>
     <height>21</height>
    </rect>
   </property>
   <property name="text">
    <string>цена</string>
   </property>
  </widget>
  <widget class="QSpinBox" name="priceEdit">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>160</y>
     <width>111</width>
     <height>22</height>
    </rect>
   </property>
   <property name="maximum">
    <number>999</number>
   </property>
  </widget>
  <widget class="QSpinBox" name="volumeEdit">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>190</y>
     <width>111</width>
     <height>22</height>
    </rect>
   </property>
   <property name="maximum">
    <number>999</number>
   </property>
  </widget>
  <widget class="QLabel" name="label_6">
   <property name="geometry">
    <rect>
     <x>130</x>
     <y>190</y>
     <width>43</width>
     <height>21</height>
    </rect>
   </property>
   <property name="text">
    <string>объём</string>
   </property>
  </widget>
  <widget class="QPushButton" name="pushButton">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>270</y>
     <width>65</width>
     <height>20</height>
    </rect>
   </property>
   <property name="text">
    <string>готово</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>"""