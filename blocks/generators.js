Blockly.Python['sonar_read'] = function(block) {
  //Blockly.Python.definitions_['import_ultrasonic'] = 'import Ultrasonic';

  var dropdown_trig = block.getFieldValue('trig');

  var code = `Ultrasonic.read(${dropdown_trig})`;
  return [code, Blockly.Python.ORDER_NONE];
};
