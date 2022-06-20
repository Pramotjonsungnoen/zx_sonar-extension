Blockly.Python['sonar_read'] = function(block) {
Blockly.Python.definitions_['import_sonar'] = 'import sonar';

  //var dropdown_trig = block.getFieldValue('trig');
  var value_seaLevelhPa = Blockly.Python.valueToCode(block, 'trig', Blockly.Python.ORDER_ATOMIC);
  //var code = `Ultrasonic.read(32)`;
  var code = `sonar.read(${value_seaLevelhPa})`;
  return [code, Blockly.Python.ORDER_NONE];
};
