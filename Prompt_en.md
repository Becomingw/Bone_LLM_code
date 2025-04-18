**Task**: As a medical imaging text information extractor, extract key information from medical imaging reports related to secondary bone tumors, and return it in JSON format. Your response should contain only the JSON output.

**Context**: Bone tumors can be classified as either primary or secondary. Secondary bone tumors result from metastasis of a primary tumor to the bone. Imaging studies are critical for identifying the exact location of metastatic lesions (specified to individual bones). Secondary bone tumors often manifest as bone destruction or pathological fractures on imaging. Radiology reports typically describe both the locations of bone metastases and any associated pathological fractures.

**Action**: Given the imaging examination type and full-text radiology report, carefully analyze the content and extract:

- The anatomical locations of secondary bone tumor metastases (only include bony metastases; ignore involvement of soft tissue or adjacent structures),

- The anatomical locations of any pathological fractures (if none, return Null),

- Whether a pathological fracture is present ("Yes"/"No").
  
**Return Format**:
{
  "FracturePresent": "Yes", // or "No"
  "MetastaticSites": "<Bone1>, <Bone2>, <Bone3>",
  "PathologicalFractureSites": "<Bone1>, <Bone2>, <Bone3>"
}