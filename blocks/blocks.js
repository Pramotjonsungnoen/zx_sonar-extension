Blockly.defineBlocksWithJsonArray([
{
  "type": "sonar_read",
  "message0": "sonar pin: %1 echo pin: %2 read distance (cm)",
  "args0": [
    {
      "type": "field_dropdown",
      "name": "trig",
      "options": [
        [
          "OUT1",
          "26"
        ],
        [
          "OUT2",
          "27"
        ],
        [
          "23",
          "23"
        ],
        [
          "19",
          "19"
        ],
        [
          "18",
          "18"
        ],
        [
          "VN",
          "39"
        ]
      ]
    }
  ],
  "output": "Number",
  "colour": "#004098",
  "tooltip": "Get data from Sony Remote",
  "helpUrl": ""
}
]);
