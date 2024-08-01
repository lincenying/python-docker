import { createApp, reactive, ref } from 'vue'

const $app$ = createApp({
    setup() {
        const fileInput = ref(null)
        const uploadStatus = ref('default')
        const selectedFile = ref(null)
        const data = ref(null)

        const onFileChange = (e) => {
            selectedFile.value = e.target.files[0];
        }

        const handleSubmit = () => {
            const formData = new FormData()
            formData.append('file', selectedFile.value, selectedFile.value.name);
            uploadStatus.value = 'uploading'
            $.ajax({
                url: '/upload?type=json',  // 替换成你的上传处理脚本
                type: 'POST',
                data: formData,
                contentType: false,
                processData: false,
                success: function(response){
                    data.value = response
                    uploadStatus.value = 'success'
                    fileInput.value.value = ''
                },
                error: function(){
                    $('#btnUpload').prop('disabled', false)
                    console.log('图片上传失败');
                }
            });
        }

        return {
            fileInput,
            uploadStatus,
            selectedFile,
            data,
            onFileChange,
            handleSubmit,
        }
    },
}).mount('#app')

window.$app$ = $app$
