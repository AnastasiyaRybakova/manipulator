
"use strict";

let SetDrawingTrajectory = require('./SetDrawingTrajectory.js')
let SetActuatorState = require('./SetActuatorState.js')
let SetKinematicsPose = require('./SetKinematicsPose.js')
let GetKinematicsPose = require('./GetKinematicsPose.js')
let GetJointPosition = require('./GetJointPosition.js')
let SetJointPosition = require('./SetJointPosition.js')

module.exports = {
  SetDrawingTrajectory: SetDrawingTrajectory,
  SetActuatorState: SetActuatorState,
  SetKinematicsPose: SetKinematicsPose,
  GetKinematicsPose: GetKinematicsPose,
  GetJointPosition: GetJointPosition,
  SetJointPosition: SetJointPosition,
};
