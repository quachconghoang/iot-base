#include "opencv2/opencv.hpp"
#include "VideosManager.h"
#include <atomic>
//#include "NvInfer.h"

cv::Mat createOne(std::vector<cv::Mat> & images, int cols, int min_gap_size);

int main()
{
    cv::cuda::setDevice(0);

    std::string filePath = std::string(getenv("HOME")) + "/IP_Camera.json";

    VideosManager videoManager;
    videoManager.loadConfigFile(filePath);
    videoManager.connectToCameras();

    std::vector<cv::Mat>  prevImages(videoManager.sessions.size());
    for (int i=0; i< videoManager.sessions.size(); i++)
        prevImages[i] = videoManager.sessions[i].h_Img;

    while (true)
    {
        for (int i=0; i< videoManager.sessions.size(); i++)
        {
            if(__globVideoThreads[i] == VS_OPENED)
            {
//                std::string nameW = std::to_string(i) + " Img";
//                cv::imshow(nameW, videoManager.sessions[i].h_Img);
                if(!videoManager.sessions[i].img_proc.empty())
                {
                    std::string nameW = std::to_string(i) + " Proc Img";
                    cv::imshow(nameW, videoManager.sessions[i].img_proc);
                    //
                }
            }
        }
        cv::Mat xxx = createOne(prevImages, 2, 2);
        cv::imshow("xxx", xxx);

        int k = cv::waitKey(30);
        if(k =='q')break;

    }
    cv::destroyAllWindows();
    videoManager.disconnect();
    std::cout<< "END GAME";
    return 0;
}


cv::Mat createOne(std::vector<cv::Mat> & images, int cols, int min_gap_size)
{
    // let's first find out the maximum dimensions
    int max_width = 0;
    int max_height = 0;
    for ( int i = 0; i < images.size(); i++) {
        // check if type is correct
        // you could actually remove that check and convert the image
        // in question to a specific type
        if ( i > 0 && images[i].type() != images[i-1].type() ) {
            std::cerr << "WARNING:createOne failed, different types of images";
            return cv::Mat();
        }
        max_height = std::max(max_height, images[i].rows);
        max_width = std::max(max_width, images[i].cols);
    }
    // number of images in y direction
    int rows = std::ceil(images.size() / cols);
    cv::Mat result = cv::Mat::zeros(rows*max_height + (rows-1)*min_gap_size,
                                    cols*max_width + (cols-1)*min_gap_size, images[0].type());
    size_t i = 0;
    int current_height = 0;
    int current_width = 0;
    for ( int y = 0; y < rows; y++ ) {
        for ( int x = 0; x < cols; x++ ) {
            if ( i >= images.size() ) // shouldn't happen, but let's be safe
                return result;
            // get the ROI in our result-image
            cv::Mat to(result,
                       cv::Range(current_height, current_height + images[i].rows),
                       cv::Range(current_width, current_width + images[i].cols));
            // copy the current image to the ROI
            images[i++].copyTo(to);
            current_width += max_width + min_gap_size;
        }
        // next line - reset width and update height
        current_width = 0;
        current_height += max_height + min_gap_size;
    }
    return result;
}