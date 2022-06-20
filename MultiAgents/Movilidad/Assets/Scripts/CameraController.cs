using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraController : MonoBehaviour
{
    //Declaracion de variables
    public GameObject[] listCamaras;
    int NUM_CAMS = 5;
    // Start is called before the first frame update
    void Start()
    {
        //Al iniciar desactivamos todas las camaras menos la principal
        for(int i=1; i<NUM_CAMS; i++){
            listCamaras[i].gameObject.SetActive(false);
        }
        listCamaras[0].gameObject.SetActive(true);
    }

    // Update is called once per frame
    void Update()
    {
        if(Input.GetKey(KeyCode.Alpha1)){
            for(int i=0; i<NUM_CAMS; i++) {
                listCamaras[i].gameObject.SetActive(false);
            }
            listCamaras[0].gameObject.SetActive(true);
        }

        if(Input.GetKey(KeyCode.Alpha2)){
            for(int i=0; i<NUM_CAMS; i++){
                listCamaras[i].gameObject.SetActive(false);
            }
            listCamaras[1].gameObject.SetActive(true);
        }

        if(Input.GetKey(KeyCode.Alpha3)){
            for(int i=0; i<NUM_CAMS; i++){
                listCamaras[i].gameObject.SetActive(false);
            }
        listCamaras[2].gameObject.SetActive(true);
        }

        if(Input.GetKey(KeyCode.Alpha4)){
            for(int i=0; i<NUM_CAMS; i++){
                listCamaras[i].gameObject.SetActive(false);
            }
        listCamaras[3].gameObject.SetActive(true);
        }

        if(Input.GetKey(KeyCode.Alpha5)){
            for(int i=0; i<NUM_CAMS; i++){
                listCamaras[i].gameObject.SetActive(false);
            }
            listCamaras[4].gameObject.SetActive(true);
        }
    }
}
